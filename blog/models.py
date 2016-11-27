from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class User(models.Model):
    User._meta.get_field('email')._unique = True

class Blogger(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    profile_pic = models.FileField(verbose_name=("Profile Picture"),
                      upload_to="images/", null=True, blank=True)
    bio = models.TextField(max_length=500, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    summary = models.TextField(max_length=100)
    image = models.FileField(upload_to='images/', blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    likes = models.ManyToManyField("Like", related_name = "post_likes")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(null=False, blank=False, max_length=300)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.body

class Category(models.Model):
    text = models.CharField(max_length=15)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

class Like(models.Model):
    user = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True)

    def counter(self, post_id):
        likes = Like.object.filter(post_id = post_id).count()
        return likes
