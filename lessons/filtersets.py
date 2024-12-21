from django_filters import rest_framework as filters
from .models import Lesson, Material


class LessonFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    course = filters.CharFilter(field_name='course__title', lookup_expr='icontains')

    class Meta:
        model = Lesson
        fields = ['title', 'course']


class MaterialFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Material
        fields = ['title', 'lesson']
