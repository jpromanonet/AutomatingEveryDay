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

def update_youtube_channel(youtube, video_id, video_description):
    request = youtube.videos().update(
        part="snippet",
        body={
            "id": video_id,
            "snippet": {
                "title": "New Blog Post Update",
                "description": video_description,
                "categoryId": "22"  # "People & Blogs" category
            }
        }
    )
    response = request.execute()
    return response

rss_feed_url = "https://your-blog-domain.com/rss-feed-url"  # Replace with your blog's RSS feed URL
video_id = "YOUR_VIDEO_ID"  # Replace with the ID of the video you want to update

youtube = setup_youtube_api()
latest_blog_post = get_latest_blog_post(rss_feed_url)
video_description = create_video_description(latest_blog_post)
update_youtube_channel(youtube, video_id, video_description)
