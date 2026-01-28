import requests
import re
from bs4 import BeautifulSoup


def scrape_wikipedia_article(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        raise Exception("Failed to fetch Wikipedia page")

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").get_text(strip=True)

    paragraphs = soup.select("div.mw-parser-output > p")

    summary_parts = []
    full_text_parts = []

    for p in paragraphs:
        text = p.get_text(" ", strip=True)

        if not text or len(text) < 40:
            continue

        full_text_parts.append(text)

        if len(summary_parts) < 3:
            summary_parts.append(text)

    raw_summary = " ".join(summary_parts)
    summary = re.sub(r"\[\d+\]", "", raw_summary)
    summary = re.sub(r"\s+", " ", summary).strip()

    full_text = " ".join(full_text_parts)

    sections = []
    for header in soup.select("div.mw-parser-output h2, div.mw-parser-output h3"):
        text = header.get_text(strip=True)
        if text and text.lower() not in ["contents", "references", "external links"]:
            sections.append(text)

    return {
        "title": title,
        "summary": summary,
        "sections": sections,
        "full_text": full_text
    }
