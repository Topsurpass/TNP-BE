from django.urls import path, include
from rest_framework import routers
from .views import UserCreateView, LogoutView


router = routers.DefaultRouter()
router.register(r'users', UserCreateView, basename='users')

user_urlpatterns = [
    path('', include(router.urls)), 
]

logout_urlpatterns = [
    path('', LogoutView.as_view(), name='token_logout'),
]