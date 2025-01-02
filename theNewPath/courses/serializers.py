from rest_framework import serializers
from .models import (
    Courses, Lesson,  Quiz, CourseCategory
)


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=CourseCategory.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Courses
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    course = CoursesSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Courses.objects.all(),
        source='course',
        write_only=True
    )

    class Meta:
        model = Lesson
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
