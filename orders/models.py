from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver
from telegram.tasks import send_order_notification


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    courses = models.ManyToManyField(Course, related_name='orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


@receiver(post_save, sender=Order)
def order_create_signal(sender, instance, created, **kwargs):

    if created:

        if hasattr(instance.user, 'telegram_account') and instance.user.telegram_account.telegram_id:
            user_id = instance.user.telegram_account.telegram_id
            send_order_notification.delay(user_id, instance.id)


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"
