from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'newsdetail.html'
    context_object_name = 'post'
