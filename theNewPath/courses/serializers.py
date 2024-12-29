from rest_framework import serializers
from .models import Courses, Lesson, UserCourse, LessonScore, Quiz, CourseCategory

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=CourseCategory.objects.all(),
        required=True,
        write_only=True
    )
    course_category = CourseCategorySerializer(source='category', read_only=True)
    
    class Meta:
        model = Courses
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(
        queryset=Courses.objects.all(),
        required=True,
        write_only=True
    )
    
    course_details = CoursesSerializer(source='course', read_only=True)
    
    class Meta:
        model = Lesson
        fields = '__all__'


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'


class LessonScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonScore
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
