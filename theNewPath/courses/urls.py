from django.urls import path, include
from rest_framework import routers
from .views import CourseCreateView, CourseCategoryView, LessonCreateView

router = routers.DefaultRouter()
router.register(r'course', CourseCreateView, basename='course')
router.register(r'course-categories', CourseCategoryView, basename='courseCategory')
router.register(r'lesson', LessonCreateView, basename='lesson')

courses_urlpatterns = [
    path('', include(router.urls)), 
]
