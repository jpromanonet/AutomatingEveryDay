import requests
import json

# Replace with your own access token
access_token = "your_access_token_here"

# Spotify Web API endpoint for searching for tracks
search_endpoint = "https://api.spotify.com/v1/search"

# Spotify Web API endpoint for adding tracks to a playlist
add_tracks_endpoint = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

# API header with the access token
header = {
    "Authorization": "Bearer " + access_token
}



