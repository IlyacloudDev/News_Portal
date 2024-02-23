from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from celery import shared_task

from News_Portal import settings

from news.models import PostCategory, Post


@shared_task
@receiver(m2m_changed, sender=PostCategory)
def post_created(id, **kwargs):

    post = Post.objects.get(pk=id)
    emails = User.objects.filter(
        subscriptions__category__in=post.category.all()
    ).values_list('email', flat=True)

    subject = f'Новый пост в категории "{post.heading}"'

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
