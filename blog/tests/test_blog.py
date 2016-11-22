from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from . import factories

#test: if index has blog posts, if can create a new post,

class BlogTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_blog_title(self):
        """
        Test that a user can search for post
        """
        # blog home page
        home_page = self.browser.get(self.live_server_url + '/')
        # site heading
        brand_element = self.browser.find_element_by_css_selector('.page-header')
        print(brand_element.text)
        self.assertEqual('Unchained Blog', brand_element.text)

    def test_index_has_posts(self):
        """
        Test if index displays the posts
        """
        home_page = self.browser.get(self.live_server_url + '/')
        post = PostFactory()
        post_element = self.browser.find_element_by_css_selector('.post a')
        self.assertEqual('Test Title', post_element.text)

    # def test_create_new_posts(self):
    #     """
    #     Test if index displays the posts
    #     """
    #     # blog home page
    #     home_page = self.browser.get(self.live_server_url + '/post/new')
    #
    #     title_input.send_keys('saxophone')
    #     instrument_input.submit()
    #     brand_element = self.browser.find_element_by_css_selector('.page-header')
    #     print(brand_element.text)
    #     self.assertEqual('Unchained Blog', brand_element.text)
