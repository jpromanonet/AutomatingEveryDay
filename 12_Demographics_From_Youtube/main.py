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

