from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .paginations import Pagination
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .trottles import Throttle



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'author__name']
    search_fields = ['title', 'content']
    pagination_class = Pagination

    throttle_classes = [AnonRateThrottle, UserRateThrottle, Throttle]
    throttle_scope = 'post_list_scope', 'post_create_scope'


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['user__name', 'skills']
    pagination_class = Pagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    pagination_class = Pagination