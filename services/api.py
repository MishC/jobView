import requests
from .generate_token import generate_token

FEED_URL = "https://pam-stilling-feed.nav.no/api/v1/feed"

def get_feed():
    token = generate_token()

    response = requests.get(
        FEED_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        },
    )

    response.raise_for_status()
    return response.json()