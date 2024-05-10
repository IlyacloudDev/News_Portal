from rest_framework import serializers

from .models import Post, Author


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
            'category'
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
            'category'
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
            'category'
        ]
