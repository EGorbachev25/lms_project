from django_filters import rest_framework as filters
from .models import Order, Payment


class OrderFilter(filters.FilterSet):
    user = filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    status = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Order
        fields = ['user', 'status']


class PaymentFilter(filters.FilterSet):
    order = filters.CharFilter(field_name='order__id')
    is_successful = filters.BooleanFilter()

    class Meta:
        model = Payment
        fields = ['order', 'is_successful']
