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

# Function to authenticate Spotify API access token
def get_token(username, client_id, client_secret, redirect_uri, scope):
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    return token

# Function to get playlist tracks
def get_tracks(username, playlist_id, token):
    sp = spotipy.Spotify(auth=token)
    tracks = []
    offset = 0
    while True:
        results = sp.user_playlist_tracks(username, playlist_id, offset=offset)
        tracks += results['items']
        offset += len(results['items'])
        if len(results['items']) == 0:
            break
    return tracks
