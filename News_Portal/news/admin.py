from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post, Category, PostCategory, Author


class PostAdmin(admin.ModelAdmin, TranslationAdmin):
    model = Post
    list_display = ('id', 'heading', 'type_of_post', 'posts_categories')
    list_filter = ('category',)
    search_fields = ('heading', 'author__authorUser__username')

    @staticmethod
    def posts_categories(p):
        return ', '.join(cat.get_name_of_category_display() for cat in p.category.all())


class CategoryAdmin(TranslationAdmin):
    model = Category


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(PostCategory)
admin.site.register(Author)
