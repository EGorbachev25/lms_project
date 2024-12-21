from django.contrib import admin
from .models import Lesson, Material


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'duration', 'created_at', 'updated_at')
    search_fields = ('title', 'course__title')
    list_filter = ('course', 'created_at')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lesson', 'created_at')
    search_fields = ('title', 'lesson__title')
    list_filter = ('created_at',)
