from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.cache import cache
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Author(models.Model):
    rating = models.FloatField(default=0.0)

    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        post_rating = self.post_set.aggregate(Sum('rating')).get('rating__sum') or 0
        comment_rating = self.authorUser.comment_set.aggregate(Sum('rating')).get('rating__sum') or 0
        compost_rating = Comment.objects.filter(post__author=self).aggregate(Sum('rating')).get('rating__sum') or 0

        self.rating = post_rating * 3 + comment_rating + compost_rating
        self.save()

    def __str__(self):
        return self.authorUser.username


class Category(models.Model):
    daily = "DA"
    sport = "SP"
    politics = "PO"
    education = "ED"
    medicine = "ME"

    POSITIONS = [
        (daily, _("Daily global news")),
        (sport, _("Sport")),
        (politics, _("Political")),
        (education, _("Education")),
        (medicine, _("Medicine")),
    ]

    name_of_category = models.CharField(max_length=2,
                                        choices=POSITIONS,
                                        unique=True,
                                        default=daily,
                                        help_text=_('category name'),
                                        )

    def __str__(self):
        return self.get_name_of_category_display()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Post(models.Model):
    article = "AR"
    news = "NE"

    POSITIONS = [
        (article, _("Article")),
        (news, _("News")),
    ]

    time_in = models.DateTimeField(auto_now_add=True)
    type_of_post = models.CharField(max_length=2,
                                    choices=POSITIONS,
                                    default=news,
                                    verbose_name=_('type of post')
                                    )
    heading = models.CharField(max_length=30, verbose_name=_('heading of post'))
    text_of_post = models.TextField(max_length=2000, verbose_name=_('text of post'))
    rating = models.FloatField(default=0.0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory', verbose_name=_('categories of posts'))

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text_of_post[:123]}...'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}') # затем удаляем его из кэша по ключу, чтобы сбросить его


class Comment(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    text_of_comment = models.TextField(max_length=255)
    rating = models.FloatField(default=0.0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
