import spotipy
import spotipy.util as util
import random
import time

# Spotify API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8000"
SCOPE = "user-read-private user-read-email user-library-read playlist-read-private playlist-modify-public"

