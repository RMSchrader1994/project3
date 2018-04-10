from django.test import TestCase
from django.urls import resolve
from .views import *

# Create your tests here.
class TestAccounts(TestCase):
    def test_cart_url_returns_ok(self):
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
    def test_cart_url_returns_view(self):
        found = resolve('/cart/')
        self.assertEqual(found.func, view_cart)