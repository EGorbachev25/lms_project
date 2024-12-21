from django.db import models
from lessons.models import Lesson
from django.contrib.auth.models import User


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='homeworks')
    students = models.ManyToManyField(User, related_name='homeworks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.title} - {self.lesson.title}"


class Submission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    file = models.FileField(upload_to='homework_submissions/', blank=True, null=True)
    comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student.username} for {self.homework.title}"


class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, related_name='grade')
    score = models.PositiveIntegerField()
    feedback = models.TextField(blank=True)
    graded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Grade: {self.score} for {self.submission.homework.title}"
