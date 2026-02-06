import datetime
import json

import requests
from cachetools import TTLCache, cached
from ddgs import DDGS
from fastmcp import FastMCP

mcp = FastMCP("WebTools")

# -------------------------------------------------------------------------
# CACHE CONFIGURATION
# -------------------------------------------------------------------------
# Weather: Cache 100 calls for 1 hour (3600 seconds)
weather_cache = TTLCache(maxsize=100, ttl=3600)

# Search: Cache 50 calls for 10 minutes (600 seconds)
search_cache = TTLCache(maxsize=50, ttl=600)

# Location: Cache 50 calls for 1 hour (3600 seconds) - Locations rarely change
location_cache = TTLCache(maxsize=50, ttl=3600)


# -------------------------------------------------------------------------
# HELPERS
# -------------------------------------------------------------------------
def serialize_datetime(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError("Type not serializable")


# -------------------------------------------------------------------------
# TOOLS
# -------------------------------------------------------------------------


@mcp.tool()
def today() -> str:
    """
    Return the current date time in ISO format.
    Use this to orient yourself in time before checking schedules or forecasts.

    Example Call: today()
    Example Result: "{'datetime': '2026-02-04 15:34:12.943265'}"
    """
    print("[LOG] Tool Execution: today")
    dt = datetime.datetime.now()
    json_data = json.dumps(dt, default=serialize_datetime)
    rv = str({"datetime", json_data})
    print(f"[LOG] Tool Execution Result: {rv}")
    return rv


@mcp.tool()
@cached(location_cache)
def get_location(city: str | None = None, country: str | None = None) -> str:
    """
    Get the latitude and longitude for a specific city or the current location.
    
    Args:
        city: The name of the city (e.g., "Aveiro").
        country: Optional country code or name (e.g., "PT" or "Portugal") to filter results.
                 If omitted, returns the current device location via IP.
    
    Example Call: get_location(city="Paris", country="France")
    Example Result: "{'name': 'Paris', 'latitude': 48.85, 'longitude': 2.35, 'country': 'France'}"
    """
    print(f"[LOG] Tool Execution: get_location (city={city}, country={country})")
    
    try:
        # 1. CURRENT LOCATION (IP-BASED)
        if not city:
            # Uses ip-api.com which is free for non-commercial use (up to 45 requests/minute)
            res = requests.get("http://ip-api.com/json/", timeout=5).json()
            if res.get("status") == "fail":
                return f"Error fetching current location: {res.get('message')}"
            
            data = {
                "name": res.get("city", "Unknown"),
                "country": res.get("countryCode", "Unknown"),
                "latitude": res.get("lat"),
                "longitude": res.get("lon"),
                "source": "current_ip"
            }
            rv = json.dumps(data)
            print(f"[LOG] Tool Execution Result: {rv}")
            return rv

        # 2. SPECIFIC CITY (GEOCODING)
        # Using Open-Meteo Geocoding API to match your weather provider
        url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {"name": city, "count": 10, "language": "en", "format": "json"}
        
        res = requests.get(url, params=params, timeout=5).json()
        
        if not res.get("results"):
            return f"Error: Could not find location '{city}'"

        results = res["results"]
        
        # Filter by country if provided
        selected_location = results[0] # Default to first result
        if country:
            country_lower = country.lower()
            for loc in results:
                # Check against country name or country code
                c_name = loc.get("country", "").lower()
                c_code = loc.get("country_code", "").lower()
                if country_lower in c_name or country_lower == c_code:
                    selected_location = loc
                    break
        
        data = {
            "name": selected_location.get("name"),
            "country": selected_location.get("country_code"),
            "latitude": selected_location.get("latitude"),
            "longitude": selected_location.get("longitude"),
            "timezone": selected_location.get("timezone"),
            "source": "geocoding_search"
        }
        
        rv = json.dumps(data)
        print(f"[LOG] Tool Execution Result: {rv}")
        return rv

    except Exception as e:
        print(f"[LOG] Tool Execution Result:\nLocation Error: {str(e)}")
        return f"Location Error: {str(e)}"


@mcp.tool()
@cached(weather_cache)
def get_weather(latitude: float, longitude: float, date: str | None = None) -> str:
    """
    Retrieve meteorological data.
    Supports current weather or 7-day forecast.

    Example Call: get_weather(latitude=40.64, longitude=-8.65)
    Example Result: "{'temperature': 18.2, 'windspeed': 12.5}"

    Args:
        latitude: GPS latitude.
        longitude: GPS longitude.
        date: Optional 'YYYY-MM-DD' string.
                If provided, returns forecast for that specific day.
                If omitted, returns current live weather
    """
    print(
        f"[LOG] Tool Execution: get_weather (lat={latitude}, lon={longitude}, date={date})"
    )
    try:
        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": "true",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",
            "timezone": "auto",
        }

        res = requests.get(url, params=params, timeout=10).json()

        if "error" in res:
            return f"API Error: {res.get('reason')}"

        # 1. Return Current Weather if no date provided
        if date is None:
            current = res.get("current_weather", {})
            rv = json.dumps(
                {
                    "type": "current_live",
                    "temperature": current.get("temperature"),
                    "windspeed": current.get("windspeed"),
                    "condition_code": current.get("weathercode"),
                }
            )
            print(f"[LOG] Tool Execution Result:\n{rv}")
            return rv

        # 2. Return Specific Day Forecast
        daily_data = res.get("daily", {})
        times = daily_data.get("time", [])

        if date not in times:
            print(
                f"""
                [LOG] Tool Execution Result:
                Error: Forecast not available for {date}.
                OpenMeteo only provides 7-day forecasts.
                """
            )
            return f"Error: Forecast not available for {date}. OpenMeteo only provides 7-day forecasts."

        index = times.index(date)
        forecast = {
            "date": date,
            "max_temp": daily_data["temperature_2m_max"][index],
            "min_temp": daily_data["temperature_2m_min"][index],
            "precipitation": daily_data["precipitation_sum"][index],
            "condition_code": daily_data["weathercode"][index],
        }
        print(f"[LOG] Tool Execution Result:\n{json.dumps(forecast)}")
        return json.dumps(forecast)

    except Exception as e:
        print(f"[LOG] Tool Execution Result:\nError fetching weather: {str(e)}")
        return f"Error fetching weather: {str(e)}"


@mcp.tool()
@cached(search_cache)
def web_search(query: str) -> str:
    """
    Execute a real-time internet search.
    Uses Google backend via DDGS for high-relevance results.

    Args:
        query: Search keywords.

    Returns:
        A list of results
    """
    print(f"[LOG] Tool Execution: web_search for '{query}'")
    try:
        results = DDGS().text(query, backend="google")
        print(f"[LOG] Tool Execution Result:\n{results}")
        rv = json.dumps(results)
        print(f"[LOG] Tool Execution Result:\n{rv}")
        return rv
    except Exception as e:
        print(f"[LOG] Tool Execution Result:\nSearch Error: {str(e)}")
        return f"Search Error: {str(e)}"


if __name__ == "__main__":
    # Start the server on a specific port (e.g., 8000)
    # Using 'sse' allows other scripts to connect via URL
    mcp.run(transport="sse", port=8000)
