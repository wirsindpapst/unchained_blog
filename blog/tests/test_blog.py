from django.test import TestCase, RequestFactory
from django.test import LiveServerTestCase
from selenium import webdriver
from blog.models import Post
from django.contrib.auth.models import User
from blog.forms import PostForm


#test: if index has blog posts, if can create a new post,

class BlogTestCase(LiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create(username="jen")
        self.post = Post.objects.create(author=self.user, title="Test title", text="Hello world!")
        self.post.publish()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_blog_title(self):
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_css_selector('.page-header')
        print(brand_element.text)
        self.assertEqual('Unchained Blog', brand_element.text)

    def test_index_has_posts(self):
        home_page = self.browser.get(self.live_server_url + '/')
        post_element = self.browser.find_element_by_css_selector('.post-title')
        self.assertEqual(self.post.title, post_element.text)

    def test_valid_form(self):
        w = Post.objects.create(title='Foo', text='Bar', author_id=self.user.id)
        data = {'title': w.title, 'text': w.text, 'author_id': w.author_id}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
