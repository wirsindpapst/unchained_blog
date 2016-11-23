from django.test import TestCase
from django.db import models
from blog.models import Comment
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User



class CommentsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='terry')
        self.post = Post.objects.create(author=self.user, title='A test blog', text="Whatever")

    def test_comment_creation(self):
        comment = Comment.objects.create(author=self.user, body="great blog!", post=self.post)
        self.assertEqual(len(Comment.objects.all()), 1)

    def test_comment_contains_text_and_assigned_to_a_user(self):
        comment = Comment.objects.create(author=self.user, body="great blog!", post=self.post)
        self.assertEqual(comment.body, "great blog!")
        self.assertEqual(comment.author, self.user)
