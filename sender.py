import requests


def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data, timeout=10)
    return response.json()


TOKEN = "7560737345:AAFW2eZy_eIU1nJ5Wok6epjr8KuQPR57MlQ"
CHAT_ID = -1002276510391
MESSAGE = "Que dahora, mensagem enviada pelo Python!"

send_telegram_message(TOKEN, CHAT_ID, MESSAGE)
