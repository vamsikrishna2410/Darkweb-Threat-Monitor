import requests
from bs4 import BeautifulSoup

def scrape_throwbin(keywords):
    print("[+] Simulating Threat Match from GitHub-hosted file...")
    
    # 👇 This points to a real file that contains your keywords
    paste_url = "https://raw.githubusercontent.com/vamsikrishna2410/Darkweb-Threat-Monitor/main/keywords.txt"
    content = requests.get(paste_url).text

    matches = []
    for keyword in keywords:
        if keyword.lower() in content.lower():
            print(f"[!] Keyword '{keyword}' found in {paste_url}")
            matches.append((paste_url, keyword))

    return matches
