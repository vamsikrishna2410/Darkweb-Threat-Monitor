import requests
from bs4 import BeautifulSoup

def scrape_throwbin(keywords):
    print("[+] Simulating Match Locally (forced test)")
    fake_paste = "https://example.com/fake-leak"
    content = "this contains password and login and secret leaked stuff"

    matches = []
    for keyword in keywords:
        if keyword.lower() in content.lower():
            print(f"[!] Keyword '{keyword}' found in {fake_paste}")
            matches.append((fake_paste, keyword))
    return matches
