import time
import os

# Simulate an AI API call with a cost and latency
def call_ai_api(prompt):
    print(f"Calling AI API with prompt: '{prompt}'...")
    # Simulate API latency
    time.sleep(1)
    # Simulate a cost associated with the call (e.g., per token, per call)
    cost_per_call = 0.10  # Example cost in USD
    print(f"AI API call finished. Cost: ${cost_per_call:.2f}")
    return f"Response for '{prompt}'", cost_per_call

# In-memory cache to store results and avoid redundant API calls
# Key: prompt, Value: (response, cost)
api_cache = {}

def get_ai_response(prompt):
    # Check if the prompt is already in the cache
    if prompt in api_cache:
        print(f"Cache hit for prompt: '{prompt}'")
        response, cost = api_cache[prompt]
        return response, 0.0  # No additional cost for cached response
    else:
        # If not in cache, call the actual AI API
        response, cost = call_ai_api(prompt)
        # Store the result in the cache for future use
        api_cache[prompt] = (response, cost)
        return response, cost

# --- Simulation --- 

print("--- First set of calls (will incur full cost) ---")

# First call for 'What is AI?'
response1, cost1 = get_ai_response("What is AI?")
print(f"Received: '{response1}', Cost: ${cost1:.2f}\n")

# First call for 'Explain machine learning'
response2, cost2 = get_ai_response("Explain machine learning")
print(f"Received: '{response2}', Cost: ${cost2:.2f}\n")

print("--- Second set of calls (should hit cache and be free) ---")

# Second call for 'What is AI?' - should be cached
response3, cost3 = get_ai_response("What is AI?")
print(f"Received: '{response3}', Cost: ${cost3:.2f}\n")

# Second call for 'Explain machine learning' - should be cached
response4, cost4 = get_ai_response("Explain machine learning")
print(f"Received: '{response4}', Cost: ${cost4:.2f}\n")

# Calculate total simulated cost
total_cost = cost1 + cost2 + cost3 + cost4
print(f"\n--- Simulation Summary ---")
print(f"Total simulated API cost without caching: ${cost1 + cost2 + 0.10 + 0.10:.2f}") # Assuming these would be called again
print(f"Total actual cost with caching: ${total_cost:.2f}")

# This example demonstrates how caching can reduce costs by avoiding repeated API calls for identical prompts.
# In a real-world scenario, you would implement more sophisticated caching strategies (e.g., TTL, disk-based caching) 
# and integrate this with your actual AI API client.
