from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

import datetime

from celery import shared_task

from News_Portal import settings
from news.models import PostCategory, Post, Category


@shared_task
def post_created(pk, **kwargs):

    post = Post.objects.get(pk=pk)
    emails = set(User.objects.filter(
        subscriptions__category__in=post.category.all()
    ).values_list('email', flat=True))
    categories_post = ', '.join([c.get_name_of_category_display() for c in post.category.all()])
    subject = f'Новый пост в категории(-ях) {categories_post}'

    text_content = (
        f'Пост: {post.heading}\n'
        f'Ссылка на пост http://127.0.0.1:8000{post.get_absolute_url()}'
    )
    html_content = (
        f'Пост: {post.heading}<br>'
        f'<a href="http://127.0.0.1:8000{post.get_absolute_url()}">'
        f'Ссылка на пост </a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task
def weekly_email():

    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('category__name_of_category', flat=True))
    subscribers = set(Category.objects.filter(name_of_category__in=categories).values_list('subscriptions__user__email', flat=True))

    html_content = render_to_string(
        'daily_posts.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
