from rest_framework.viewsets import ModelViewSet
from .models import Forum, Topic, Comment
from .serializers import ForumSerializer, TopicSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ForumViewSet(ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'user__username']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['text', 'user__username', 'topic__title']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
