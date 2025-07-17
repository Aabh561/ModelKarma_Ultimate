import requests

BOT_TOKEN = "7117388468:AAHuSG6GnsbpKj1FL2sQkDJkQzgi5HBTiko"
CHAT_ID = "6298447721"

def send_telegram_alert(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("✅ Telegram alert sent.")
    except Exception as e:
        print(f"❌ Failed to send Telegram alert: {e}")

