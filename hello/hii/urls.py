from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('profiles', ProfileViewSet, basename='profile')
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]