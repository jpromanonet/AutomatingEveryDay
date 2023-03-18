import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Enter your Spotify app client ID, client secret, and redirect URL here
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'your_redirect_uri'

# Set the scope for the Spotify Web API
SCOPE = 'playlist-modify-public'

# Set the name and description for the new playlist
PLAYLIST_NAME = 'My Mood Playlist'
PLAYLIST_DESCRIPTION = 'A playlist for when I need some good vibes'

# Set the mood or occasion for the playlist
MOOD = 'happy'

# Set the number of tracks to add to the playlist
TRACKS_LIMIT = 20

# Initialize the Spotify Web API client with the Spotipy library
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

# Search for tracks based on the mood or occasion
results = sp.search(q=MOOD, limit=TRACKS_LIMIT, type='track')

# Create a list of track URIs
track_uris = []
for track in results['tracks']['items']:
    track_uris.append(track['uri'])

# Create a new public playlist with the given name and description
playlist = sp.user_playlist_create(user=sp.me()['id'], name=PLAYLIST_NAME, public=True, description=PLAYLIST_DESCRIPTION)

# Add the tracks to the new playlist
sp.user_playlist_add_tracks(user=sp.me()['id'], playlist_id=playlist['id'], tracks=track_uris)
