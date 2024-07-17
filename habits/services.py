import requests
from config.settings import BOT_TOKEN


def send_telegram_message(chat_id, message):  # интеграция с Телеграмм
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params=params)
