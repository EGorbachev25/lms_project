from django_filters import rest_framework as filters
from .models import Homework, Submission, Grade


class HomeworkFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    lesson = filters.CharFilter(field_name='lesson__title', lookup_expr='icontains')

    class Meta:
        model = Homework
        fields = ['title', 'lesson']


class SubmissionFilter(filters.FilterSet):
    student = filters.CharFilter(field_name='student__username', lookup_expr='icontains')

    class Meta:
        model = Submission
        fields = ['student', 'homework']


class GradeFilter(filters.FilterSet):
    score = filters.NumberFilter()

    class Meta:
        model = Grade
        fields = ['score']
