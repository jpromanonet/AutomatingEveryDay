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

# Select a random artist from the top artists
random_artist = random.choice(top_artists['items'])

# Create a personalized message using the random track and artist
message = f"Hey there! We noticed you've been listening to {random_track['name']} by {random_track['artists'][0]['name']} a lot lately. Did you know that {random_artist['name']} is a similar artist you might enjoy? Check them out and let us know what you think!"
