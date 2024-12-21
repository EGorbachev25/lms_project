from rest_framework.viewsets import ModelViewSet
from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer
from .filtersets import CourseFilter, ReviewFilter
from django_filters.rest_framework import DjangoFilterBackend


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter
