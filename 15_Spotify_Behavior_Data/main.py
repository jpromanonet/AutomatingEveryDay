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

def get_playlists_based_on_artists(top_artists, limit):
    playlists = []
    for artist in top_artists['items']:
        search_results = sp.search(q=artist['name'], type='playlist', limit=limit)
        playlists.extend(search_results['playlists']['items'])
    return playlists

def get_tracks_from_playlists(playlists):
    all_tracks = []
    for playlist in playlists:
        tracks = sp.playlist_tracks(playlist['id'])
        all_tracks.extend(tracks['items'])
    return all_tracks
