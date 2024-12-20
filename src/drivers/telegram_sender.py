import requests


def send_telegram_message(message):
    token = "7560737345:AAFW2eZy_eIU1nJ5Wok6epjr8KuQPR57MlQ"
    chat_id = -1002276510391
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload, timeout=10)
