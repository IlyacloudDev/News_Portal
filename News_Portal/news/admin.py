from django.contrib import admin
from .models import Post, Category, PostCategory, Author, User


# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Author)
admin.register(User)
