def scrape_local_file(keywords):
    print("[+] Reading from local test file...")

    matches = []
    with open('test_paste.txt', 'r') as file:
        content = file.read()
        for keyword in keywords:
            if keyword.lower() in content.lower():
                print(f"[!] Keyword '{keyword}' found in test_paste.txt")
                matches.append(('test_paste.txt', keyword))
    return matches
