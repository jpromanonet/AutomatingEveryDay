import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

# Set up authentication using the Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your_client_id",
                                               client_secret="your_client_secret",
                                               redirect_uri="your_redirect_uri",
                                               scope="user-read-recently-played user-top-read"))

# Get the user's recently played tracks
recent_tracks = sp.current_user_recently_played(limit=50)

# Get the user's top artists
top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')

# Select a random track from the recently played tracks
random_track = random.choice(recent_tracks['items'])


