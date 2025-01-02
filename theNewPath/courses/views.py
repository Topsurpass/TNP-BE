from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Courses, CourseCategory, Lesson, Quiz
from .serializers import (
    CoursesSerializer,
    CourseCategorySerializer,
    LessonSerializer,
    QuizSerializer,
)
from .pagination import CustomPageNumberPagination



class CourseCreateView(viewsets.ModelViewSet):
    """
    API view for listing, creating, and modifying courses.
    """
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    @action(detail=True, methods=["get"])
    def lessons(self, request, pk=None):
        course = self.get_object()
        lessons = course.lessons.all()
        paginator = CustomPageNumberPagination()
        paginated_lessons = paginator.paginate_queryset(lessons, request)
        serializer = LessonSerializer(paginated_lessons, many=True)
        return paginator.get_paginated_response(serializer.data)


class CourseCategoryView(viewsets.ModelViewSet):
    """
    API view for listing, creating, and modifying course categories.
    """
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

    @action(detail=True, methods=["get"])
    def courses(self, request, pk=None):
        category = self.get_object()
        courses = category.courses_in_category.all()
        paginator = CustomPageNumberPagination()
        paginated_courses = paginator.paginate_queryset(courses, request)
        serializer = CoursesSerializer(paginated_courses, many=True)
        return paginator.get_paginated_response(serializer.data)


class LessonCreateView(viewsets.ModelViewSet):
    """
    API view for listing, creating, and modifying lessons.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    @action(detail=True, methods=["get", "post"])
    def quizzes(self, request, pk=None):
        lesson = self.get_object()

        if request.method == "GET":
            quizzes = lesson.quizzes.all()
            paginator = CustomPageNumberPagination()
            paginated_quizzes = paginator.paginate_queryset(quizzes, request)
            serializer = QuizSerializer(paginated_quizzes, many=True)
            return paginator.get_paginated_response(serializer.data)

        elif request.method == "POST":
            data = request.data.copy()
            data['lesson'] = lesson.lesson_id
            serializer = QuizSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizViewSet(viewsets.ModelViewSet):
    """
    API view for managing quizzes.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
