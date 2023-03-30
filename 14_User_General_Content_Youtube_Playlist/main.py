# Setup your YouTube data API Client
from googleapiclient.discovery import build

api_key = "YOUR_API_KEY"
youtube = build("youtube", "v3", developerKey=api_key)

# Search for user content and channels
def search_youtube(query, max_results=25):
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=max_results,
        type="video",
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        videos.append(search_result)

    return videos

# Create a playlist
def create_playlist(title, description, privacy_status="public"):
    body = {
        "snippet": {
            "title": title,
            "description": description,
        },
        "status": {
            "privacyStatus": privacy_status,
        },
    }

    response = youtube.playlists().insert(
        part="snippet,status",
        body=body,
    ).execute()

    return response["id"]

# Add videos to a playlist
def add_video_to_playlist(playlist_id, video_id):
    body = {
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": video_id,
            },
        },
    }

    response = youtube.playlistItems().insert(
        part="snippet",
        body=body,
    ).execute()

    return response
