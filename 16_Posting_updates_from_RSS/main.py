import os
import feedparser
import datetime
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

def setup_youtube_api():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
    return youtube

def get_latest_blog_post(rss_feed_url):
    feed = feedparser.parse(rss_feed_url)
    latest_post = feed.entries[0]
    return latest_post

def create_video_description(blog_post):
    title = blog_post.title
    link = blog_post.link
    description = f"Check out our latest blog post: {title}\nRead the full article: {link}"
    return description
