from rest_framework import serializers
from .models import Lesson, Material


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'
