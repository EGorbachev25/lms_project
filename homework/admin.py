from django.contrib import admin
from .models import Homework, Submission, Grade


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lesson', 'due_date', 'created_at')
    search_fields = ('title', 'lesson__title')
    list_filter = ('lesson', 'due_date')


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'homework', 'student', 'submitted_at')
    search_fields = ('student__username', 'homework__title')
    list_filter = ('submitted_at',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'submission', 'score', 'graded_at')
    search_fields = ('submission__homework__title', 'submission__student__username')
    list_filter = ('graded_at',)
