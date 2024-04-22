from .models import Category, Post
from modeltranslation.translator import register, TranslationOptions # импортируем декоратор для перевода и класс


# настроек, от которого будем наследоваться
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name_of_category', ) # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('type_of_post', 'heading', 'text_of_post', 'category') # указываем, какие именно поля надо переводить в виде кортежа
