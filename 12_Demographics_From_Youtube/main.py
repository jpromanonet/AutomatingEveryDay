import google.auth
import google.auth.transport.requests
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set API credentials
API_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRETS_FILE = "client_secrets.json"

# Set video ID
VIDEO_ID = "your_video_id"

# Authenticate API access
def authenticate():
    credentials = None
    try:
        credentials = google.auth.load_credentials_from_file(
            "credentials.json",
            scopes=["https://www.googleapis.com/auth/youtube.readonly"],
        )
    except Exception:
        credentials = None
    if not credentials or not credentials.valid:
        flow = google.auth.transport.requests.Request()
        flow.credentials = google.oauth2.credentials.Credentials.from_authorized_user_file(
            "credentials.json", scopes=["https://www.googleapis.com/auth/youtube.readonly"]
        )
        credentials = flow.credentials
    return credentials

# Retrieve video statistics
def get_video_statistics(youtube, video_id):
    results = youtube.videos().list(
        part="statistics",
        id=video_id
    ).execute()
    for item in results["items"]:
        print(f"Video view count: {item['statistics']['viewCount']}")
        print(f"Video like count: {item['statistics']['likeCount']}")
        print(f"Video dislike count: {item['statistics']['dislikeCount']}")
        print(f"Video comment count: {item['statistics']['commentCount']}")

