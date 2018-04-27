from django.test import TestCase
from django.urls import resolve
from .views import *

# Create your tests here.
class TestAccounts(TestCase):
    def test_products_url_returns_ok(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 302)
    def test_login_url_returns_view(self):
        found = resolve('/products/')
        self.assertEqual(found.func, get_dlc)