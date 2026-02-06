import asyncio
import uuid

from flask import Flask, jsonify, request
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
from mcp.types import TextContent

import ollama

app = Flask(__name__)
MODEL = "granite4:latest"
SYSTEM_PROMPT = """
You are a helpful assistant with access to real-time tools.
1. Use Markdown for formatting (bold, lists, code blocks).
2. If a user asks for weather or web info, use the tools.
3. Summarize tool results concisely.
4. Maintain a helpful and professional tone.
"""

chat_history = {}


async def run_agent_async(session_id, user_query):
    if session_id not in chat_history:
        chat_history[session_id] = [{"role": "system", "content": SYSTEM_PROMPT}]

    chat_history[session_id].append({"role": "user", "content": user_query})
    messages = chat_history[session_id]
    steps = []

    async with sse_client("http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. Discover tools
            tools_resp = await session.list_tools()
            available_tools = [
                {
                    "type": "function",
                    "function": {
                        "name": t.name,
                        "description": t.description,
                        "parameters": t.inputSchema,
                    },
                }
                for t in tools_resp.tools
            ]

            # 2. Start the Agent Loop
            # We loop until the model stops calling tools or hits a limit
            MAX_ITERATIONS = 5
            for _ in range(MAX_ITERATIONS):
                
                # Call Ollama with current history
                response = ollama.chat(
                    model=MODEL, messages=messages, tools=available_tools
                )
                
                # Check if the model wants to talk or call a tool
                if not response.message.tool_calls:
                    # No tools called? This is the final answer.
                    final_answer = response.message.content
                    steps.append({"role": "final", "content": final_answer})
                    messages.append({"role": "assistant", "content": final_answer})
                    break  # EXIT THE LOOP

                # If we are here, tools were called.
                # Add the assistant's "intent" to history so it knows what it asked for
                messages.append(response.message)
                steps.append({
                    "role": "assistant",
                    "content": response.message.content or "Calling tools..."
                })

                # Process all tool calls in this batch
                for tool in response.message.tool_calls:
                    tool_args = dict(tool.function.arguments)
                    
                    # Log for UI
                    steps.append({
                        "role": "tool_call",
                        "name": tool.function.name,
                        "args": tool.function.arguments,
                    })

                    # Execute Tool via MCP
                    result = await session.call_tool(tool.function.name, tool_args)
                    
                    tool_output = ""
                    for content in result.content:
                        if isinstance(content, TextContent):
                            tool_output += content.text

                    steps.append({"role": "tool_result", "result": tool_output})

                    # Add result to history so LLM sees it next iteration
                    messages.append({
                        "role": "tool",
                        "content": tool_output,
                        "name": tool.function.name,
                    })

    return steps


@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")
    session_id = data.get("session_id")

    if not session_id:
        session_id = str(uuid.uuid4())

    steps = asyncio.run(run_agent_async(session_id, query))
    return jsonify(steps=steps, session_id=session_id)


if __name__ == "__main__":
    app.run(port=5000)
