from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


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


class Category(models.Model):
    daily = "DA"
    sport = "SP"
    politics = "PO"
    education = "ED"
    medicine = "ME"

    POSITIONS = [
        (daily, "Ежедневные глобальные новости"),
        (sport, "Спорт"),
        (politics, "Политика"),
        (education, "Образование"),
        (medicine, "Медицина"),
    ]

    name_of_category = models.CharField(max_length=2,
                                        choices=POSITIONS,
                                        unique=True,
                                        default=daily)


class Post(models.Model):
    article = "AR"
    news = "NE"

    POSITIONS = [
        (article, "Статья"),
        (news, "Новость"),
    ]

    time_in = models.DateTimeField(auto_now_add=True)
    type_of_post = models.CharField(max_length=2,
                                    choices=POSITIONS,
                                    default=news
                                    )
    heading = models.CharField(max_length=30)
    text_of_post = models.TextField(max_length=2000)
    rating = models.FloatField(default=0.0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text_of_post[:123]}...'


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
