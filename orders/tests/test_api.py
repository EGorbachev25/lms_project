from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Order


class OrderAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.order = Order.objects.create(user=self.user, status='pending')

    def test_list_orders(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        data = {'user': self.user.id, 'status': 'paid'}
        response = self.client.post('/api/orders/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
