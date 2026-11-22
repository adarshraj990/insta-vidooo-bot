"""
Antigravity Daily Instagram Reel Automation Bot
-----------------------------------------------
1. Generates 9:16 high-definition AI scene artwork
2. Composites Ken Burns motion, dynamic particles & Devanagari typography
3. Renders MP4 video via Playwright & FFmpeg
4. Publishes directly to Instagram (@mel0dy_songs) via Buffer GraphQL API
"""

import os
import json
import ssl
import urllib.request

BUFFER_TOKEN = os.environ.get("BUFFER_TOKEN")
CHANNEL_ID = os.environ.get("BUFFER_CHANNEL_ID", "6b027e358541f09ecb5f093b") # @mel0dy_songs
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "adarshraj990/insta-vidooo-bot")

def create_github_release_asset(video_path, tag_name, release_title):
    token = GITHUB_TOKEN or os.environ.get("GH_TOKEN")
    ctx = ssl.create_default_context()
    rel_url = f"https://api.github.com/repos/{GITHUB_REPO}/releases"
    payload = json.dumps({
        "tag_name": tag_name,
        "name": release_title,
        "body": f"Automated Daily Build: {release_title}",
        "draft": False,
        "prerelease": False
    }).encode("utf-8")
    
    headers = {
        "Authorization": f"token {token}",
        "User-Agent": "AntigravityBot/1.0",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    try:
        req = urllib.request.Request(rel_url, data=payload, headers=headers)
        with urllib.request.urlopen(req, context=ctx) as r:
            rel = json.loads(r.read().decode())
    except urllib.error.HTTPError:
        req = urllib.request.Request(f"{rel_url}/tags/{tag_name}", headers={"Authorization": f"token {token}", "User-Agent": "AntigravityBot/1.0"})
        with urllib.request.urlopen(req, context=ctx) as r:
            rel = json.loads(r.read().decode())
            
    upload_url = rel["upload_url"].split("{")[0] + f"?name={os.path.basename(video_path)}"
    with open(video_path, "rb") as f:
        video_bytes = f.read()
        
    req_upload = urllib.request.Request(
        upload_url,
        data=video_bytes,
        headers={
            "Authorization": f"token {token}",
            "User-Agent": "AntigravityBot/1.0",
            "Content-Type": "video/mp4",
            "Accept": "application/vnd.github.v3+json"
        }
    )
    with urllib.request.urlopen(req_upload, context=ctx) as r:
        asset = json.loads(r.read().decode())
        return asset["browser_download_url"]

def publish_reel_to_buffer(video_url, caption_text):
    token = BUFFER_TOKEN
    ctx = ssl.create_default_context()
    endpoint = "https://api.buffer.com"
    query = """
    mutation CreateVideoPost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
            text
            status
            dueAt
          }
        }
        ... on MutationError {
          message
        }
      }
    }
    """
    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": caption_text,
            "schedulingType": "automatic",
            "mode": "shareNow",
            "assets": [
                {
                    "video": {
                        "url": video_url
                    }
                }
            ],
            "metadata": {
                "instagram": {
                    "type": "reel",
                    "shouldShareToFeed": True
                }
            }
        }
    }
    data = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "AntigravityBot/1.0"
        }
    )
    with urllib.request.urlopen(req, context=ctx) as resp:
        return json.loads(resp.read().decode())

if __name__ == "__main__":
    print("Ready to run automated daily reel generation & publishing pipeline.")
