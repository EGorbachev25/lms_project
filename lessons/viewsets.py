from rest_framework.viewsets import ModelViewSet
from .models import Lesson, Material
from .serializers import LessonSerializer, MaterialSerializer
from .filtersets import LessonFilter, MaterialFilter
from django_filters.rest_framework import DjangoFilterBackend


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LessonFilter


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MaterialFilter
