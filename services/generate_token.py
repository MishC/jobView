import re
import requests

TOKEN_URL = "https://pam-stilling-feed.nav.no/api/publicToken"

def generate_token() -> str:
    raw = requests.get(TOKEN_URL).text.replace("\n", "").replace("\r", "")
    match = re.search(r"eyJ.*?_nwFcE", raw)

    if not match:
        raise ValueError("NAV token not found")

    return match.group(0)