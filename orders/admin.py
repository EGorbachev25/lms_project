from django.contrib import admin
from .models import Order, Payment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('status', 'created_at')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'payment_date', 'is_successful')
    search_fields = ('order__id',)
    list_filter = ('is_successful', 'payment_date')
