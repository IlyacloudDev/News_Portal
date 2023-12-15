from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class NewsForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['heading', 'text_of_post', 'category', 'author']

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get('heading')
        text_of_post = cleaned_data.get('text_of_post')

        if len(heading) > 40:
            raise ValidationError({
                'heading': 'Заголовок не должен быть больше 50 символов'
            })
        if text_of_post == heading:
            raise ValidationError({
                'Заголовок не должен быть идентичен тексту'
            })


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['heading', 'text_of_post', 'category', 'author']

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get('heading')
        text_of_post = cleaned_data.get('text_of_post')

        if len(heading) > 40:
            raise ValidationError({
                'heading': 'Заголовок не должен быть больше 50 символов'
            })
        if text_of_post == heading:
            raise ValidationError({
                'Заголовок не должен быть идентичен тексту'
            })
