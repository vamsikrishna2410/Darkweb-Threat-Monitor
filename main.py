from scrapers.pastebin_scraper import scrape_pastebin, load_keywords
from alerts.telegram_alert import send_telegram_alert

if __name__ == "__main__":
    keywords = load_keywords()
    results = scrape_pastebin(keywords)
    print("\nMatched Results:")
    for url, kw in results:
        print(f" - Keyword '{kw}' found in {url}")
