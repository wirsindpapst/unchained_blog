from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(models.Model):
    User._meta.get_field('email')._unique = True

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
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

class Category(models.Model):
    text = models.CharField(max_length=15)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.body

class Category_post(models.Model):
    category = models.ForeignKey(Category)
    post = models.ForeignKey(Post)
