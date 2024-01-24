import requests
import json

TOKEN = "<YOUR_TOKEN>"
ORG = "ChargeMap"
API_VERSION = "2022-11-28"
BASE_URL = f"https://api.github.com/orgs/{ORG}/repos"

print("Starting the script...")

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": API_VERSION,
}

page = 1

while True:
    response = requests.get(f"{BASE_URL}?per_page=100&page={page}", headers=headers)
    response_json = response.json()

    if not response_json:
        print(f"No more repositories to list : {json.dumps(response_json)}")
        break

    for item in response_json:
        print(f"- {item['full_name']}")

    page += 1

print("Script completed.")
