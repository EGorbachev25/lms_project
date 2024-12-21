from django.db import models
from courses.models import Course


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.title} ({self.course.title})"


class Material(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='lesson_materials/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
