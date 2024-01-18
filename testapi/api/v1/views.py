from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from django.contrib.auth.models import User

from .serializers import TestSerializers, PostSerializers, CategorySerializers
from ...models import Test, Post, Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['^name']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__id']
    search_fields = ['title']


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['^name']
