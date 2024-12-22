from celery import shared_task
from telegram.service import send_telegram_message


@shared_task(bind=True)
def send_order_notification(self, user_id, order_id):
    message = f"Order {order_id} was successfully created!"
    send_telegram_message(user_id, message)
    return f"Notification sent for Order {order_id}"
