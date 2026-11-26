import os
import json
import ssl
import urllib.request
from datetime import datetime

BUFFER_TOKEN = os.environ.get("BUFFER_TOKEN", "VeuPLEC4vfP2JzaQw-cFpa_MTrTLTcA6yplvwnNXhd6")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "6b027e358541f09ecb5f093b")

ctx = ssl.create_default_context()

query = """
query GetChannelPosts($channelId: RecordID!) {
  channel(id: $channelId) {
    id
    serviceId
    posts(input: { filter: { status: scheduled } }) {
      totalCount
      edges {
        node {
          id
          status
          dueAt
          text
        }
      }
    }
  }
}
"""

req = urllib.request.Request(
    "https://api.buffer.com",
    data=json.dumps({"query": query, "variables": {"channelId": CHANNEL_ID}}).encode('utf-8'),
    headers={
        "Authorization": f"Bearer {BUFFER_TOKEN}",
        "Content-Type": "application/json"
    }
)

try:
    with urllib.request.urlopen(req, context=ctx) as r:
        data = json.loads(r.read().decode('utf-8'))
        channel = data.get('data', {}).get('channel', {})
        posts_info = channel.get('posts', {})
        total_scheduled = posts_info.get('totalCount', 0)
        edges = posts_info.get('edges', [])

        print(f"=== BUFFER CLOUD AUTOPILOT MONITOR ===")
        print(f"Timestamp: {datetime.utcnow().isoformat()} UTC")
        print(f"Active Scheduled Posts in Cloud Queue: {total_scheduled}")
        print("-" * 50)

        for edge in edges:
            node = edge['node']
            due_at = node.get('dueAt')
            first_line = node.get('text', '').split('\n')[0]
            print(f"[LIVE IN BUFFER CLOUD] {due_at} -> {first_line}")

        if total_scheduled >= 4:
            print("\n[OK] Queue is healthy! Posts are queued in Buffer Cloud.")
        else:
            print(f"\n[ALERT] Queue has only {total_scheduled} posts remaining. Advance scheduling needed.")

except Exception as e:
    print(f"Error querying Buffer API: {e}")
    exit(1)
