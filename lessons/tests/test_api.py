from rest_framework.test import APITestCase
from rest_framework import status
from lessons.models import Lesson, Material
from courses.models import Course


class LessonAPITestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(title="Test Course", description="A test course", price=10.0)
        self.lesson = Lesson.objects.create(
            title="Test Lesson", course=self.course, duration=60, description="Test Lesson Description"
        )

    def test_list_lessons(self):
        response = self.client.get('/api/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MaterialAPITestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(title="Test Course", description="A test course", price=10.0)
        self.lesson = Lesson.objects.create(
            title="Test Lesson", course=self.course, duration=60, description="Test Lesson Description"
        )
        self.material = Material.objects.create(
            title="Test Material", lesson=self.lesson, link="http://example.com"
        )

    def test_list_materials(self):
        response = self.client.get('/api/materials/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
