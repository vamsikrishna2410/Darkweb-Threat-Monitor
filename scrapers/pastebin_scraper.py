import requests
from bs4 import BeautifulSoup

def load_keywords():
    with open('keywords.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]

def scrape_pastebin(keywords):
    print("[+] Scraping Pastebin...")
    url = "https://pastebin.com/archive"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pastes = soup.select("table.maintable tr td a[href^='/']")
    print(f"[DEBUG] Found {len(pastes)} pastes")

    matches = []
    for p in pastes[:5]:  # Limit to latest 5 pastes
        paste_id = p['href'].lstrip('/')
        paste_url = f"https://pastebin.com/raw/{paste_id}"
        print(f"[>] Scanning: {paste_url}")  # ✅ This now prints
        content_page = requests.get(paste_url)
        if "Sorry" in content_page.text or "404" in content_page.text:
            continue
        for keyword in keywords:
            if keyword.lower() in content_page.text.lower():
                print(f"[!] Keyword '{keyword}' found in {paste_url}")
                matches.append((paste_url, keyword))

    return matches
