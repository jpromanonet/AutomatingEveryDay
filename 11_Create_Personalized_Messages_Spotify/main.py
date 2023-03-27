import spotipy
import spotipy.util as util
import random
import time

# Spotify API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8000"
SCOPE = "user-read-private user-read-email user-library-read playlist-read-private playlist-modify-public"

# User credentials
USERNAME = "your_spotify_username"
PLAYLIST_ID = "your_playlist_id"

# Personalized message template
message_template = "Hey {name}, thanks for listening to my playlist! I would really appreciate it if you could leave a review and let me know what you think. Thanks again!"


