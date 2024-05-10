from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializers import PostSerializer, NewsSerializer, ArticleSerializer, CategorySerializer, AuthorSerializer, UserSerializer
from .models import Post, Author, Category


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class NewsViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(type_of_post='NE')
    serializer_class = NewsSerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(type_of_post='AR')
    serializer_class = ArticleSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
