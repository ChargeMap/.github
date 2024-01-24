import requests
import json

TOKEN = "<YOUR_TOKEN>"
ORG = "ChargeMap"
TEAM_SLUG = "back-end-php"
OWNER = "ChargeMap"
API_VERSION = "2022-11-28"
BASE_URL = f"https://api.github.com/orgs/{ORG}/teams/{TEAM_SLUG}/repos"

repos = ["community-optkjhgkjghins"]

print("Starting the script...")

for repo in repos:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": API_VERSION,
    }

    data = {"permission": "admin"}

    response = requests.put(f"{BASE_URL}/{OWNER}/{repo}", headers=headers, json=data)
    response_json = response.json()

    if response.status_code == 204:
        print(f"Repository '{repo}' successfully added to team: '{TEAM_SLUG}'")
    else:
        print(f"Failed to add repository '{repo}' to team: '{TEAM_SLUG}' ({response.status_code} : {json.dumps(response_json)})")

print("Script completed.")
