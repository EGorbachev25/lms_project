from rest_framework import serializers
from .models import Homework, Submission, Grade


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
