from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        self.driver.implicitly_wait(20)
        self.driver.get("http://127.0.0.1:8000/accounts/register/")
        self.driver.find_element_by_id('id_username').send_keys('Test42111')
        self.driver.find_element_by_id('id_email').send_keys('test@test.com')
        self.driver.find_element_by_id('id_password1').send_keys('Unchained')
        self.driver.find_element_by_id('id_password2').send_keys('Unchained')
        self.driver.find_element_by_id('sign_up').click()
        bodyText = self.driver.find_element_by_id('message').text
        self.assertEqual("Thanks for registering. You are now logged in.", bodyText)

    def test_user_uses_exisiting_name(self):
        self.driver.implicitly_wait(20)
        self.driver.get("http://127.0.0.1:8000/accounts/register/")
        self.driver.find_element_by_id('id_username').send_keys('Test')
        self.driver.find_element_by_id('id_email').send_keys('test@test.com')
        self.driver.find_element_by_id('id_password1').send_keys('Unchained')
        self.driver.find_element_by_id('id_password2').send_keys('Unchained')
        self.driver.find_element_by_id('sign_up').click()
        bodyText = self.driver.find_elements_by_class_name('errorlist')[0].text
        self.assertEqual("A user with that username already exists.", bodyText)



if __name__ == '__main__':
    unittest.main()
