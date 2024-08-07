"""
URL configuration for News_Portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import routers
from news import viewsets


router = routers.DefaultRouter()
router.register(r'posts', viewsets.PostViewset)
router.register(r'news', viewsets.NewsViewset, basename='news')
router.register(r'articles', viewsets.ArticleViewset, basename='articles')
router.register(r'categories', viewsets.CategoryViewset)
router.register(r'authors', viewsets.AuthorViewset)
router.register(r'users', viewsets.UserViewset)


urlpatterns = [
    path('admin/', admin.site.urls),

    # DRF configuration
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # OpenAPI specification
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

    # allauth extension
    path('accounts/', include('allauth.urls')),

    # own custom apps
    path('', include('news.urls')),
    path('subscriptions/', include('subscriptions.urls')),

    # i18n extension
    path('i18n/', include('django.conf.urls.i18n')),

]
