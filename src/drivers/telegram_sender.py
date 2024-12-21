import requests


def send_telegram_message(message):
    token = "<token_telegram>"
    chat_id = 0 # chat-id telegram
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload, timeout=10)
