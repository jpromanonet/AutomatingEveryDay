# Setup your YouTube data API Client
from googleapiclient.discovery import build

api_key = "YOUR_API_KEY"
youtube = build("youtube", "v3", developerKey=api_key)
