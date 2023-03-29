import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from textblob import TextBlob

# Set up Spotify API credentials
os.environ["SPOTIPY_CLIENT_ID"] = "your_spotify_client_id"
os.environ["SPOTIPY_CLIENT_SECRET"] = "your_spotify_client_secret"
os.environ["SPOTIPY_REDIRECT_URI"] = "your_spotify_redirect_uri"

