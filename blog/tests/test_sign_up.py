from django.test import TestCase
from selenium import webdriver

class NewUserTestCase(TestCase):
    def test_register_page(self):
        resp = self.client.get('/accounts/register/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'<h1>Sign Up!</h1>', resp.content)

    def test_user_registration(self):
