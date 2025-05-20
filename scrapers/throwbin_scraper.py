import requests
from bs4 import BeautifulSoup

def scrape_throwbin(keywords):
    print("[+] Scraping Throwbin...")
    url = "https://www.throwbin.io/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.select("a[href^='/paste/']")

    matches = []
    for link in links[:5]:
        paste_id = link['href'].split('/')[-1]
        paste_url = f"https://www.throwbin.io/paste/{paste_id}"
        print(f"[>] Scanning: {paste_url}")
        content = requests.get(paste_url).text
        for keyword in keywords:
            if keyword.lower() in content.lower():
                print(f"[!] Keyword '{keyword}' found in {paste_url}")
                matches.append((paste_url, keyword))
    return matches

