from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import (EmailMultiAlternatives, mail_managers, mail_admins)


# создали кастомный сопсоб регистрации на основе существующего в пакете allauth
class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name='common users')
        # теперь при успешной регистрации (только если через email и пароль)
        # пользователь будет добавляться в группу common users
        user.groups.add(common_users)

        # механизм отправки письма нашему успешно зарегестрированному пользователю
        subject = 'Добро пожаловать в наш интернет-магазин!'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/posts">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        return user
