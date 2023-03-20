import os
import google.auth
import googleapiclient.discovery

def upload_video(video_file, video_title, video_description):
    # Authenticate and construct the YouTube API client
    credentials, project_id = google.auth.default()
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    # Define the video metadata
    video_metadata = {
        "snippet": {
            "title": video_title,
            "description": video_description,
            "categoryId": 22
        },
        "status": {
            "privacyStatus": "private"
        }
    }
