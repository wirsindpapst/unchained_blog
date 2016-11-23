from django.test import TestCase, RequestFactory
from django.test import LiveServerTestCase
from selenium import webdriver
from blog.models import Comment
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User

class BlogTestCase(LiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create(username='june')
        self.post = Post.objects.create(author=self.user, title='A test blog', text="Whatever")
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()


    def test_comments_can_be_created_in_the_browser(self):
        """
        Need do build in form elements once live - not currently a proper feature test yet
        """
        self.browser.get(self.live_server_url + "/accounts/register/")
        self.browser.find_element_by_id('id_username').send_keys('Test234354343')
        self.browser.find_element_by_id('id_email').send_keys('test@test.com')
        self.browser.find_element_by_id('id_password1').send_keys('Unchained')
        self.browser.find_element_by_id('id_password2').send_keys('Unchained')
        self.browser.find_element_by_id('sign_up').click()
        post_id = self.post.id
        test_page = self.browser.get(self.live_server_url + '/post/' + str(post_id))
        test_text = "Test comment #1"
        self.browser.find_element_by_id('id_body').send_keys(test_text)
        self.browser.find_element_by_id('post_comment_btn').click()
        self.browser.implicitly_wait(3)
        test_page = self.browser.get(self.live_server_url + '/post/' + str(post_id))
        self.browser.get(self.live_server_url + '/')
        test_page = self.browser.get(self.live_server_url + '/post/' + str(post_id))
        target_text = self.browser.find_element_by_id('comment-body')
        self.assertEqual(target_text, test_text)
