from django.db import models
from django.contrib.auth.models import User


class TelegramUserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='telegram_account')
    telegram_id = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.user.username}'s Telegram Account"
