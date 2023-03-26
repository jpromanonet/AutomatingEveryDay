import requests
import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up News API key and endpoint
NEWS_API_KEY = 'your_news_api_key_here'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

# Set up YouTube API credentials and endpoint
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
CLIENT_SECRETS_FILE = 'client_secrets.json'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Set up video metadata
VIDEO_TITLE = 'Latest News Update'
VIDEO_DESCRIPTION = 'This video provides a summary of the latest news articles from News API.'

# Set up YouTube video upload parameters
YOUTUBE_UPLOAD_PARAMS = {
    'part': 'snippet,status',
    'body': {
        'snippet': {
            'title': VIDEO_TITLE,
            'description': VIDEO_DESCRIPTION
        },
        'status': {
            'privacyStatus': 'public'
        }
    },
    'media_body': None
}

# Set up YouTube credentials
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = Credentials.from_authorized_user_info(json.load(token), SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        token.write(json.dumps(creds.to_authorized_user_info()))

# Fetch the latest news articles
response = requests.get(NEWS_API_ENDPOINT, params={'apiKey': NEWS_API_KEY})
news_articles = response.json()['articles']

# Create a YouTube API client
youtube = build(API_SERVICE_NAME, API_VERSION, credentials=creds)

# Upload each news article as a video to YouTube
for article in news_articles:
    # Fetch article information
    article_title = article['title']
    article_description = article['description']
    article_url = article['url']
    article_image_url = article['urlToImage']
    
    # Download article image
    image_response = requests.get(article_image_url)
    with open('article_image.jpg', 'wb') as f:
        f.write(image_response.content)
    
    # Set video metadata
    YOUTUBE_UPLOAD_PARAMS['body']['snippet']['title'] = article_title
    YOUTUBE_UPLOAD_PARAMS['body']['snippet']['description'] = article_description
    
    # Upload video to YouTube
    try:
        YOUTUBE_UPLOAD_PARAMS['media_body'] = MediaFileUpload('article_image.jpg')
        youtube.videos().insert(
            **YOUTUBE_UPLOAD_PARAMS
        ).execute()
    except HttpError as error:
        print(f'An error occurred: {error}')
        continue
