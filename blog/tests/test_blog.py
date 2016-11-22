from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver

class BlogTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_user_find_posts(self):
        """
        Test that a user can search for post
        """
        # blog home page
        home_page = self.browser.get(self.live_server_url + '/')
        # site heading
        brand_element = self.browser.find_element_by_css_selector('.page-header')
        print(brand_element.text)
        self.assertEqual('Unchained Blog', brand_element.text)
