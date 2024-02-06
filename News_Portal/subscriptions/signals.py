from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from news.models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if kwargs['action'] != 'post_add':
        return

    emails = User.objects.filter(
        subscriptions__category__in=instance.postCategory
    ).values_list('email', flat=True)

    subject = f'Новый пост в категории "{instance.heading}"'

    text_content = (
        f'Пост: {instance.post_id.heading}\n'
        f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Пост: {instance.post_id.heading}<br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на пост: </a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
