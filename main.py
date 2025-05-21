from scrapers.local_scraper import scrape_local_file
from scrapers.pastebin_scraper import load_keywords

print("🧠 [MAIN] This is the REAL main.py running")


if __name__ == "__main__":
    keywords = load_keywords()
    results = scrape_local_file(keywords)
    print("\nMatched Results:")
    if not results:
        print("No matches found.")
    for url, kw in results:
        print(f" - Keyword '{kw}' found in {url}")

