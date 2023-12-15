from django.urls import path
# Импортируем созданное нами представление
from .views import (PostList, PostDetail,
                    PostSearch, NewsCreate,
                    NewsUpdate, NewsDelete,
                    ArticleCreate, ArticleUpdate,
                    ArticleDelete,)


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='posts_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),

   path('news/create/', NewsCreate.as_view(), name='news_creating'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_updating'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_deleting'),

   path('articles/create/', ArticleCreate.as_view(), name='article_creating'),
   path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_updating'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_deleting'),
]
