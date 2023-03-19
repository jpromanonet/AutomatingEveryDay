import requests
from bs4 import BeautifulSoup

# Set the URL of the YouTube video you want to scrape
url = "https://www.youtube.com/watch?v=VIDEO_ID"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the video title
title = soup.find('span', attrs={'class': 'watch-title'}).text.strip()

# Extract the video description
description = soup.find('div', attrs={'class': 'watch-description'}).text.strip()

# Extract the video tags
tags = [tag.text.strip() for tag in soup.find_all('meta', attrs={'property': 'og:video:tag'})]

# Extract the view count
view_count = soup.find('div', attrs={'class': 'watch-view-count'}).text.strip()

# Extract the like and dislike counts
likes = soup.find('button', attrs={'title': 'I like this'}).text.strip()
dislikes = soup.find('button', attrs={'title': 'I dislike this'}).text.strip()

# Print the extracted data
print('Title:', title)
print('Description:', description)
print('Tags:', tags)
print('View count:', view_count)
print('Likes:', likes)
print('Dislikes:', dislikes)

# Extract comments from the video
comments_url = f"https://www.youtube.com/all_comments?v=VIDEO_ID"
comments_response = requests.get(comments_url)
comments_soup = BeautifulSoup(comments_response.content, 'html.parser')

# Extract comment text and username
comments = []
for comment in comments_soup.find_all('div', {'class': 'comment-renderer-text-content'}):
    username = comment.find('a', {'class': 'yt-uix-sessionlink spf-link'}).text.strip()
    text = comment.find('div', {'class': 'comment-renderer-text'}).text.strip()
    comments.append({'username': username, 'text': text})

# Print the extracted comments
print('Comments:')
for comment in comments:
    print(comment['username'], '-', comment['text'])
