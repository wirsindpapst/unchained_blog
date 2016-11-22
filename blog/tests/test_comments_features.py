from django.test import TestCase, RequestFactory
from django.test import LiveServerTestCase
from selenium import webdriver
from blog.models import Comment
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User






class BlogTestCase(LiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create(username='terry')
        self.post = Post.objects.create(author=self.user, title='A test blog', text="Whatever")
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_comments_render_to_page(self):
        """
        Need do build in form elements once live
        """
        comment = Comment.objects.create(author=self.user, body="great blog!", post=self.post)
        test_page = self.browser.get(self.live_server_url + 'post/1/')
        print(self.post.title)
        target_text = self.browser.find_element_by_css_selector('.comment-body')
        self.assertEqual(comment.body, target_text.text)
