from django.urls import path, include
from rest_framework import routers
from .views import (
    CourseCreateView,
    CourseCategoryView,
    LessonCreateView,
    # LessonScoreViewSet,
    QuizViewSet
)

router = routers.DefaultRouter()
router.register(r'courses', CourseCreateView, basename='courses')
router.register(r'course-categories', CourseCategoryView, basename='courseCategory')
router.register(r'lessons', LessonCreateView, basename='lessons')
# router.register(r'lesson-scores', LessonScoreViewSet, basename='lesson-scores')
router.register(r'quizzes', QuizViewSet, basename='quizzes')


courses_urlpatterns = [
    path('', include(router.urls)), 
]
