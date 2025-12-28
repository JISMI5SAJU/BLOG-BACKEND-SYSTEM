from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Blog!")


# Root/test view
def root_view(request):
    return JsonResponse({"message": "Welcome to the Blog API!"})

def test_view(request):
    return JsonResponse({"message": "Blog app is working!"})

# -------------------------------
# REST framework imports and views
# -------------------------------
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer, CommentSerializer, RegisterSerializer

# Register user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# BlogPost CRUD
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Comment CRUD
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
