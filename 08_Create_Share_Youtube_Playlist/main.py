import requests
import json

# Replace with your own API key
api_key = "your_api_key_here"

# YouTube Data API endpoint for searching for videos
search_endpoint = "https://www.googleapis.com/youtube/v3/search"

# YouTube Data API endpoint for creating a new playlist
playlist_endpoint = "https://www.googleapis.com/youtube/v3/playlists"

# Function to search for videos based on a keyword or phrase
def search_videos(q):
    params = {
        "q": q,
        "part": "snippet",
        "type": "video",
        "key": api_key
    }
    response = requests.get(search_endpoint, params=params)
    return response.json()

# Function to create a new playlist
def create_playlist(title):
    data = {
        "snippet": {
            "title": title
        }
    }
    response = requests.post(playlist_endpoint, params={"part": "snippet", "key": api_key}, json=data)
    return response.json()

