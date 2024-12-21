from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from forums.models import Forum


class ForumAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.forum = Forum.objects.create(name='Test Forum')

    def test_list_forums(self):
        response = self.client.get('/api/forums/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_forum(self):
        data = {'name': 'New Forum'}
        response = self.client.post('/api/forums/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
