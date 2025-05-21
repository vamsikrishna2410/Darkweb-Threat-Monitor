import requests

def send_telegram_alert(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        r = requests.post(url, data=payload)
        if r.status_code != 200:
            print(f"[!] Failed to send alert: {r.text}")
        else:
            print("[+] Telegram alert sent!")
    except Exception as e:
        print(f"[!] Telegram error: {e}")

