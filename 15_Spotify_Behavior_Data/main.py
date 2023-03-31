import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_CLIENT_SECRET",
                                               redirect_uri="YOUR_REDIRECT_URI",
                                               scope="user-top-read"))

def get_user_top_tracks_and_artists(time_range, limit):
    top_tracks = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    top_artists = sp.current_user_top_artists(time_range=time_range, limit=limit)
    return top_tracks, top_artists
