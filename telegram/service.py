import os
import requests
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def send_telegram_message(user_id, message):
    resp = requests.post(
        f'https://api.telegram.org/bot{TOKEN}/sendMessage',
        json={
            'chat_id': user_id,
            'text': message
        }
    )
    print(resp.json())
    return resp.json()


def set_webhook():
    resp = requests.post(
        f'https://api.telegram.org/bot{TOKEN}/setWebhook',
        json={
            'url': 'https://354a-189-202-12-273.ngrok-free.app/telegram'
        }
    )
    print(resp.json())
