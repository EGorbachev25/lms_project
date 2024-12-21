from django.contrib import admin
from .models import Forum, Topic, Comment


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'forum', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('forum', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'topic', 'created_at')
    search_fields = ('user__username', 'topic__title')
    list_filter = ('created_at',)

