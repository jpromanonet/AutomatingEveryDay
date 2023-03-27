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

# Function to send personalized messages
def send_messages(tracks, message_template, token):
    sp = spotipy.Spotify(auth=token)
    for track in tracks:
        # Get track listener details
        listener = track['added_by']['id']
        response = sp.user(listener)
        name = response['display_name']
        email = response['email']
        # Personalize message
        message = message_template.format(name=name)
        # Send message
        print("Sending message to {}...".format(email))
        time.sleep(random.randint(1, 5))  # Add delay to avoid spamming
        # Uncomment the following line to send email
        # send_email(email, message)
        # Uncomment the following line to send SMS
        # send_sms(phone_number, message)

# Main program
if __name__ == '__main__':
    # Authenticate Spotify API access token
    token = get_token(USERNAME, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE)
    if token:
        # Get playlist tracks
        tracks = get_tracks(USERNAME, PLAYLIST_ID, token)
        # Send personalized messages
        send_messages(tracks, message_template, token)
    else:
        print("Can't get token for", USERNAME)
