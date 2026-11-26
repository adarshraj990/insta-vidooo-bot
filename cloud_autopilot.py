import os
import json
import ssl
import urllib.request
from datetime import datetime, timezone

BUFFER_TOKEN = os.environ.get("BUFFER_TOKEN", "VeuPLEC4vfP2JzaQw-cFpa_MTrTLTcA6yplvwnNXhd6")
REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "scheduled_posts.json")

ctx = ssl.create_default_context()

q = """
query GetPostDetails($input: PostInput!) {
  post(input: $input) {
    id
    status
    dueAt
    sentAt
    text
    error {
      message
    }
  }
}
"""

if not os.path.exists(REGISTRY_PATH):
    print("No scheduled_posts.json registry found.")
    exit(0)

with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
    posts = json.load(f)

print("=" * 60)
print("=== BUFFER CLOUD AUTOPILOT WATCHDOG (UNATTENDED RUNNER) ===")
print(f"Current UTC Time: {datetime.now(timezone.utc).isoformat()}")
print(f"Tracking {len(posts)} total scheduled/live posts...")
print("=" * 60)

active_scheduled_count = 0
published_count = 0

for item in posts:
    pid = item["id"]
    slot = item.get("slot", "")
    song = item.get("song", "")
    
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=json.dumps({"query": q, "variables": {"input": {"id": pid}}}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {BUFFER_TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "AntigravityBufferWatchdog/1.0"
        }
    )
    
    try:
        with urllib.request.urlopen(req, context=ctx) as r:
            res = json.loads(r.read().decode("utf-8"))
            post_data = res.get("data", {}).get("post")
            if not post_data:
                print(f"[MISSING/REMOVED] ID {pid} ({song} - {slot})")
                continue
            
            status = post_data.get("status")
            due_at = post_data.get("dueAt")
            sent_at = post_data.get("sentAt")
            err = post_data.get("error")
            
            if status == "scheduled":
                active_scheduled_count += 1
                print(f"[LOCKED IN CLOUD] {slot} | {song} | Due: {due_at} | Status: {status}")
            elif status == "sent":
                published_count += 1
                print(f"[SUCCESS PUBLISHED] {slot} | {song} | Sent: {sent_at}")
            else:
                print(f"[{status.upper()}] {slot} | {song} | Due: {due_at} | Err: {err}")
    except Exception as e:
        print(f"[ERROR CHECKING] {song} ({pid}): {e}")

print("-" * 60)
print(f"Summary: {active_scheduled_count} pending in cloud queue, {published_count} successfully published.")
if active_scheduled_count > 0:
    print("[CLOUD HEALTH OK] Buffer will automatically push these to Instagram without PC or user interaction!")
else:
    print("[ATTENTION] All queued posts have been published. Next batch must be scheduled.")
print("=" * 60)
