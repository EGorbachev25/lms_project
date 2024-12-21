from rest_framework.test import APITestCase
from rest_framework import status
from courses.models import Course, Review
from django.contrib.auth.models import User


class CourseAPITestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(title="Test Course", description="A test course", price=10.0)

    def test_list_courses(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReviewAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.course = Course.objects.create(title="Test Course", description="A test course", price=10.0)
        self.client.login(username="testuser", password="password")

    def test_create_review(self):
        data = {"course": self.course.id, "user": self.user.id, "text": "Great!", "rating": 5}
        response = self.client.post('/api/reviews/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
