from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Post
from .serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer, VideoSerializer
from .permissions import IsAuthorOrAdmin, IsAuthor
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class StandartPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'count': self.page.paginator.count,
            'results': data
        })

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = StandartPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return PostCreateSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [IsAuthorOrAdmin()]
        return [IsAuthenticated()]


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PostCreateSerializer
        return PostListSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == "DELETE":
            return (IsAuthorOrAdmin(),)
        elif self.request.method in ["PUT", "PATCH"]:
            return (IsAuthor(),)
        return (AllowAny(),)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostCreateSerializer
        return PostDetailSerializer

class VideoCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = VideoSerializer


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = VideoSerializer



