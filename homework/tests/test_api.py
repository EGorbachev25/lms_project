from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from homework.models import Homework
from lessons.models import Lesson


class HomeworkAPITestCase(APITestCase):

    def setUp(self):
        self.lesson = Lesson.objects.create(title="Lesson 1")
        self.homework = Homework.objects.create(title="Homework 1", lesson=self.lesson)

    def test_list_homework(self):
        response = self.client.get('/api/homework/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
