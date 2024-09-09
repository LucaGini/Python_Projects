import requests
import sys

GITHUB_API_URL = "https://api.github.com/users/{}/events"

def get_user_activity(username):
    try:
        response = requests.get(GITHUB_API_URL.format(username))
        response.raise_for_status() # Raise an exception for 4xx/5xx status codes
        events = response.json()
        return events
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user activity: {e}")
        return None

def display_activity(events):
    if not events:
        print("No activity found.")
        return

    for event in events:
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        
        if event_type == "PushEvent":
            print(f"- Pushed {len(event['payload']['commits'])} commits to {repo_name}")
        elif event_type == "IssuesEvent":
            print(f"- Opened a new issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
        else:
            print(f"- {event_type} on {repo_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    events = get_user_activity(username)
    display_activity(events)