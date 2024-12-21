from django.contrib import admin
from .models import Course, Review


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user', 'rating', 'created_at')
    search_fields = ('user__username', 'course__title')
    list_filter = ('rating', 'created_at')
