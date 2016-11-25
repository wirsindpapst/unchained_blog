from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(models.Model):
    User._meta.get_field('email')._unique = True

    # def create_profile(sender, **kwargs):
    #     user = kwargs["instance"]
    #     if kwargs["created"]:
    #         user_profile = Blogger(user=user)
    #         user_profile.save()
    # post_save.connect(create_profile, sender=User)

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
    image = models.FileField(upload_to='images/', blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.body
