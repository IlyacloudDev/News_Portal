from rest_framework import viewsets

from .serializers import PostSerializer, NewsSerializer, ArticleSerializer
from .models import Post, Author


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class NewsViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(type_of_post='NE')
    serializer_class = NewsSerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(type_of_post='AR')
    serializer_class = ArticleSerializer
