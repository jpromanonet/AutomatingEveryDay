import requests
import json

# Replace with your own API key
api_key = "your_api_key_here"

# YouTube Data API endpoint for retrieving channel information
channel_endpoint = "https://www.googleapis.com/youtube/v3/channels"

# YouTube Data API endpoint for retrieving subscriber information
subscriber_endpoint = "https://www.googleapis.com/youtube/v3/subscriptions"

# Function to retrieve channel information based on a channel ID or username
def get_channel_info(channel_id_or_username):
    params = {
        "part": "snippet,statistics",
        "key": api_key
    }
    if channel_id_or_username.startswith("UC"):
        params["id"] = channel_id_or_username
    else:
        params["forUsername"] = channel_id_or_username
    response = requests.get(channel_endpoint, params=params)
    return response.json()
