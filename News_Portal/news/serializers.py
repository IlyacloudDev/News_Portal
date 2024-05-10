from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, Author, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'time_in',
            'type_of_post',
            'heading',
            'text_of_post',
            'rating',
            'author',
            'category',
        ]


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'time_in',
            'type_of_post',
            'heading',
            'text_of_post',
            'rating',
            'author',
            'category',
        ]


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'time_in',
            'type_of_post',
            'heading',
            'text_of_post',
            'rating',
            'author',
            'category',
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name_of_category',
        ]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'rating',
            'authorUser',
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]
