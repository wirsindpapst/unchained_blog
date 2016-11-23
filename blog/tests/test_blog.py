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
        self.browser.get(self.live_server_url + '/')


    def tearDown(self):
        self.browser.quit()

    def test_blog_title(self):
        title_element = self.browser.find_element_by_css_selector('.page-header')
        self.assertEqual('Unchained Blog', title_element.text)

    def test_index_has_posts(self):
        home_page = self.browser.get(self.live_server_url + '/')
        post_element = self.browser.find_element_by_css_selector('.post-title')
        self.assertEqual(self.post.title, post_element.text)

    def test_valid_form(self):
        w = Post.objects.create(title='Foo', text='Bar', author_id=self.user.id)
        data = {'title': w.title, 'text': w.text, 'author_id': w.author_id}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_user_can_add_post(self):
        self.browser.implicitly_wait(20)
        self.browser.get(self.live_server_url + '/accounts/register')
        self.browser.find_element_by_id('id_username').send_keys('TestUser')
        self.browser.find_element_by_id('id_email').send_keys('test@test.com')
        self.browser.find_element_by_id('id_password1').send_keys('Unchained')
        self.browser.find_element_by_id('id_password2').send_keys('Unchained')
        self.browser.find_element_by_id('sign_up').click()
        self.browser.find_element_by_class_name('top-menu').click()
        self.browser.find_element_by_id('id_title').send_keys('New post')
        self.browser.find_element_by_id('id_text').send_keys('This is a test post.')
        self.browser.find_element_by_class_name('save').click()
        # print(self.browser.find element ecc(body))
        post_title_element = self.browser.find_element_by_id('post-detail-title')
        self.assertEqual('New post', post_title_element.text)
