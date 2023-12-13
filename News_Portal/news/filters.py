from django_filters import (FilterSet, DateTimeFilter, CharFilter)
from django import forms
from .models import Post


class PostFilter(FilterSet):
    heading = CharFilter(
        label='Heading',
        lookup_expr='iregex'
    )

    time_after = DateTimeFilter(
        label='Post was created earlier than:',
        field_name='time_in',
        lookup_expr='gt',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = ['type_of_post']
