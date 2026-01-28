import requests
import validators
from bs4 import BeautifulSoup

def validate_wikipedia_url(url: str):
    # 1. Basic URL validation
    if not validators.url(url):
        return False, "Invalid URL format"

    # 2. Wikipedia domain check
    if "wikipedia.org/wiki/" not in url:
        return False, "URL must be a Wikipedia article link"

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; DeepKlarityBot/1.0)"
    }

    # 3. Try fetching page
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return False, "Wikipedia page not reachable"
    except Exception:
        return False, "Error fetching the URL"

    # 4. Extract article title (preview)
    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("h1", {"id": "firstHeading"})

    if not title_tag:
        return False, "Could not extract article title"

    return True, title_tag.text.strip()
