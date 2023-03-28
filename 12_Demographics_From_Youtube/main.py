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

