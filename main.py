from scrapers.pastebin_scraper import scrape_pastebin, load_keywords
from alerts.telegram_alert import send_telegram_alert
from logger import log_to_csv

BOT_TOKEN = "7807793284:AAFG_t1X2O6jNY3P3RpL-fuNd0wsoLqhbz8"
CHAT_ID = "965209658"

if __name__ == "__main__":
    keywords = load_keywords()
    results = scrape_pastebin(keywords)
    print("\nMatched Results:")
    send_telegram_alert(BOT_TOKEN, CHAT_ID, "✅ Test alert from my bot!")
    for url, kw in results:
        message = f"⚠️ Keyword *'{kw}'* found in {url}"
        print(f" - {message}")
        send_telegram_alert(BOT_TOKEN, CHAT_ID, message)

