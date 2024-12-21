from rest_framework.viewsets import ModelViewSet
from .models import Order, Payment
from .serializers import OrderSerializer, PaymentSerializer
from .filtersets import OrderFilter, PaymentFilter
from django_filters.rest_framework import DjangoFilterBackend


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
