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

    # Upload the video file
    request = youtube.videos().insert(
        part="snippet,status",
        body=video_metadata,
        media_body=video_file
    )
    response = request.execute()

    # Print the response
    print("Video was uploaded successfully:", response)

if __name__ == "__main__":
    video_file = os.path.join("path", "to", "video", "file.mp4")
    video_title = "My video title"
    video_description = "My video description"
    upload_video(video_file, video_title, video_description)
