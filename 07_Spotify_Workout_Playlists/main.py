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

# Function to search for tracks based on a keyword or phrase
def search_tracks(q):
    params = {
        "q": q,
        "type": "track"
    }
    response = requests.get(search_endpoint, headers=header, params=params)
    return response.json()

# Function to add tracks to a playlist
def add_tracks_to_playlist(playlist_id, track_uris):
    data = {
        "uris": track_uris
    }
    response = requests.post(add_tracks_endpoint.format(playlist_id=playlist_id), headers=header, json=data)
    return response.json()

# Main function to automate the process of updating your personal Spotify playlist based on your workout or exercise routine
def main():
    # Example code to search for tracks based on your workout or exercise routine
    workout_type = "running"
    search_results = search_tracks("fast-paced energetic music for " + workout_type)

    # Example code to add the tracks you're interested in to your playlist
    playlist_id = "your_playlist_id_here"
    track_uris = [track["uri"] for track in search_results["tracks"]["items"]]
    add_tracks_to_playlist(playlist_id, track_uris)

if __name__ == "__main__":
    main()
