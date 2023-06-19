# %%
import requests

# %%
# Define the base URL for the FastAPI application
base_url = "http://localhost:8000"
# %%
# Function to send a POST request to add an item to the queue
def add_item_to_queue(item):
    url = f"{base_url}/add_item/{item}"
    response = requests.post(url)
    if response.status_code == 200:
        print("Item added to the queue successfully.")
    else:
        print("Failed to add item to the queue.")
# %%
# Send a POST request to add an item to the queue
add_item_to_queue("example_item")

# %%
