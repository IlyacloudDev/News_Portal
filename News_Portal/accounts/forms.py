from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


# создали кастомный сопсоб регистрации на основе существующего в пакете allauth
class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name='common users')
        user.groups.add(common_users)
        return user
        # теперь при успешной регистрации (только если через email и пароль) пользователь будет добавляться в группу common users
