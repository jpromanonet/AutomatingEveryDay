import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

# Authenticate with Spotify API using your client ID and secret
client_id = 'your_client_id'
client_secret = 'your_client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get total number of followers
followers = sp.current_user_followers()
total_followers = followers['total']

# Get number of tracks saved by followers
saved_tracks = sp.current_user_saved_tracks()
total_saved_tracks = saved_tracks['total']

# Get top artists and tracks of followers
top_artists = sp.current_user_top_artists(time_range='short_term', limit=10)
top_tracks = sp.current_user_top_tracks(time_range='short_term', limit=10)

# Get country of the user
user = sp.current_user()
country = user['country']

# Get followed artists by followers
followed_artists = sp.current_user_followed_artists(limit=10)

# Create a dictionary with the retrieved information
data = {'Total Followers': [total_followers],
        'Total Saved Tracks': [total_saved_tracks],
        'Top Artists': [', '.join([artist['name'] for artist in top_artists['items']])],
        'Top Tracks': [', '.join([track['name'] for track in top_tracks['items']])],
        'Country': [country],
        'Followed Artists': [', '.join([artist['name'] for artist in followed_artists['artists']['items']])]
       }

# Convert the dictionary to a Pandas dataframe and generate a report
df = pd.DataFrame(data)
report = df.to_markdown(index=False)

# Print the report
print(report)
