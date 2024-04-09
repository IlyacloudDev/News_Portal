from django.contrib import admin
from .models import Post, Category, PostCategory, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'type_of_post', 'posts_categories')
    list_filter = ('category',)
    search_fields = ('heading', 'author__authorUser__username')

    @staticmethod
    def posts_categories(p):
        return ', '.join(cat.get_name_of_category_display() for cat in p.category.all())


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Author)
