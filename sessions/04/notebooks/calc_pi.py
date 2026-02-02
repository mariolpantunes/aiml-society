import random
import math
import time

def estimate_pi(num_iterations):
    num_inside_circle = 0
    
    start_time = time.time()
    
    for _ in range(num_iterations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        
        if distance <= 1:
            num_inside_circle += 1
    
    end_time = time.time()
    
    pi_estimate = (num_inside_circle / num_iterations) * 4
    print(f"Estimated Pi: {pi_estimate}")
    print(f"Actual Pi: {math.pi}")
    print(f"Time taken: {end_time - start_time} seconds")
    return pi_estimate

estimate_pi(100000)