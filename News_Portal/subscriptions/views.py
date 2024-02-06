from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.views.decorators.csrf import csrf_protect

from .models import Subscriber
from news.models import Category


# Create your views here.
@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscriber.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscriber.objects.filter(
                user=request.user,
                category=category
            ).delete()

    # Мы соберём все категории постов с сортировкой по алфавиту и добавим специальное поле, которое покажет,
    # подписан сейчас пользователь на данную категорию или нет.
    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscriber.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name_of_category')
    return render(
        request,
        'subscriptions/subscriptions.html',
        {'categories': categories_with_subscriptions},
        )
