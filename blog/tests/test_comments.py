from django.test import TestCase
from django.db import models
from blog.models import Comment
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User



class CommentsTestCase(TestCase):
    def test_comment_creation(self):
        me = User.objects.create(username='terry')
        post = Post.objects.create(author=me, title='A test blog', text="Whatever")
        comment = Comment.objects.create(author=me, body="great blog!", post=post)
        self.assertEqual(len(Comment.objects.all()), 1)

    def test_comment_contains_text(self):
        me = User.objects.create(username='terry')
        post = Post.objects.create(author=me, title='A test blog', text="Whatever")
        comment = Comment.objects.create(author=me, body="great blog!", post=post)
        self.assertEqual(comment.body, "great blog!")
        self.assertEqual(comment.author, me)

    # def test_comment_deletion(self):
    #     me = User.objects.create(username='terry')
    #     post = Post.objects.create(author=me, title='A test blog', text="Whatever")
    #     comment = Comment.objects.create(author=me, body="great blog!", post=post)
    #
    #     self.assertEqual(len(Comment.objects.all()), 1)
