import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from textblob import TextBlob

# Set up Spotify API credentials
os.environ["SPOTIPY_CLIENT_ID"] = "your_spotify_client_id"
os.environ["SPOTIPY_CLIENT_SECRET"] = "your_spotify_client_secret"
os.environ["SPOTIPY_REDIRECT_URI"] = "your_spotify_redirect_uri"

# Get user input for mood
mood_input = input("How are you feeling today? ")

# Analyze the sentiment of the mood input
sentiment = TextBlob(mood_input).sentiment.polarity

# Set the mood category
if sentiment > 0.5:
    mood_category = "happy"
elif sentiment > 0:
    mood_category = "neutral"
else:
    mood_category = "sad"

# Spotify authentication
scope = "playlist-modify-public"
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Replace with your own Spotify username and playlist ID
username = "your_spotify_username"
playlist_id = "your_playlist_id"

# Search for tracks based on the mood category
track_results = sp.search(q=f"{mood_category}", type="track", limit=20)

# Extract track IDs
track_ids = [track["id"] for track in track_results["tracks"]["items"]]

# Clear the existing playlist
sp.playlist_replace_items(playlist_id, [])

# Add the new tracks to the playlist
sp.playlist_add_items(playlist_id, track_ids)

print(f"Your playlist has been updated with {mood_category} songs!")
