import pytz

from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (View, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.cache import cache
from django.utils import timezone

from .models import Post
from .filters import PostFilter
from .forms import NewsForm, ArticleForm
from .mixins import TimezoneMixin

from subscriptions.tasks import post_created


# Create your views here.


# class Index(View):
#     def get(self, request):
#         string = _('Hello world')
#
#         return HttpResponse(string)


class PostList(TimezoneMixin, ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts_info/posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'posts_info/post_detail.html'
    context_object_name = 'post'

    def get_object(self, *args, **kwargs): # переопределяем метод получения объекта, как ни странно

        obj = cache.get(f'post-{self.kwargs["pk"]}', None) # кэш очень похож на словарь, и метод get действует так же.
        # Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj


class PostSearch(TimezoneMixin, ListView):
    model = Post
    template_name = 'posts_info/post_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'article_news_actions/news_update.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.type_of_post = Post.news
        post.save()
        post_created.delay(post.pk)
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'article_news_actions/news_update.html'

    def form_valid(self, form):
        form.instance.type_of_post = Post.news
        return super().form_valid(form)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'article_news_actions/news_delete.html'
    success_url = reverse_lazy('posts_list')


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = ArticleForm
    model = Post
    template_name = 'article_news_actions/article_update.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.type_of_post = Post.article
        post.save()
        post_created.delay(post.pk)
        return super().form_valid(form)


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = ArticleForm
    model = Post
    template_name = 'article_news_actions/article_update.html'

    def form_valid(self, form):
        form.instance.type_of_post = Post.article
        return super().form_valid(form)


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'article_news_actions/article_delete.html'
    success_url = reverse_lazy('posts_list')
