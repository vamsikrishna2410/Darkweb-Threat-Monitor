from scrapers.local_scraper import scrape_local_file, load_keywords

if __name__ == "__main__":
    keywords = load_keywords()
    results = scrape_local_file(keywords)
    print("\nMatched Results:")
    for url, kw in results:
        print(f" - Keyword '{kw}' found in {url}")
