from rest_framework.viewsets import ModelViewSet
from .models import Homework, Submission, Grade
from .serializers import HomeworkSerializer, SubmissionSerializer, GradeSerializer
from .filtersets import HomeworkFilter, SubmissionFilter, GradeFilter
from django_filters.rest_framework import DjangoFilterBackend


class HomeworkViewSet(ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HomeworkFilter


class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubmissionFilter


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GradeFilter
