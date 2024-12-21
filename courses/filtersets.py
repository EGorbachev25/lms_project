from django_filters import rest_framework as filters
from .models import Course, Review


class CourseFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    price = filters.RangeFilter()

    class Meta:
        model = Course
        fields = ['title', 'price']


class ReviewFilter(filters.FilterSet):
    rating = filters.RangeFilter()

    class Meta:
        model = Review
        fields = ['rating', 'course']
