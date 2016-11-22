from django.test import TestCase
from selenium import webdriver
# import unittest



class NewUserTestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_register_page(self):
        resp = self.client.get('/accounts/register/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'<h1>Sign Up!</h1>', resp.content)


    def test_user_registration(self):
        self.driver.get("http://127.0.0.1:8000/accounts/register/")
        self.driver.find_element_by_id('id_username').send_keys('Test234354343')
        self.driver.find_element_by_id('id_email').send_keys('test@test.com')
        self.driver.find_element_by_id('id_password1').send_keys('Unchained')
        self.driver.find_element_by_id('id_password2').send_keys('Unchained')
        self.driver.find_element_by_id('sign_up').click()
        # self.assertIn("http://127.0.0.1:8000", self.driver.current_url)
        bodyText = self.driver.find_element_by_tag_name('body').text
        self.assertEqual("Thanks for registering. You are now logged in.", bodyText)



if __name__ == '__main__':
    unittest.main()
