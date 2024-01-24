#!/bin/bash

TOKEN="<YOUR_TOKEN>"
ORG="ChargeMap"
TEAM_SLUG="back-end-php"
OWNER="ChargeMap"
API_VERSION="2022-11-28"
BASE_URL="https://api.github.com/orgs/$ORG/teams/$TEAM_SLUG/repos"

repos=("community-optins")

echo "Starting the script..."

for repo in "${repos[@]}"; do

  # Use a try-catch mechanism
  response=$(curl -s -w "%{http_code}" \
      -X PUT \
      -H "Accept: application/vnd.github+json" \
      -H "Authorization: Bearer $TOKEN" \
      -H "X-GitHub-Api-Version: $API_VERSION" \
      -d '{"permission":"admin"}' \
      "$BASE_URL/$OWNER/$repo")

  if [ "$status_code" -eq 200 ]; then
      echo "Repository '$repo' successfully added to team: '$TEAM_SLUG'"
  else
      echo "Failed to add repository '$repo' to team: '$TEAM_SLUG' (HTTP Status Code: $status_code)"
  fi
done

echo "Script completed."
