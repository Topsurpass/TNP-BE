from rest_framework import viewsets
from .models import  Courses, CourseCategory, Lesson
from .serializers import  CoursesSerializer, CourseCategorySerializer, LessonSerializer


class CourseCreateView(viewsets.ModelViewSet):
    """Api view for listing, creating and modifying a course."""
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    
class CourseCategoryView(viewsets.ModelViewSet):
    """Api view for listing, creating and modifying a course category."""
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    
class LessonCreateView(viewsets.ModelViewSet):
    """Api view for listing, creating and modifying a lesson."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
