from django.apps import apps
from django.test import TestCase
from .apps import CartConfig

class TestcartConfig(TestCase):
    def test_cart_app(self):
        self.assertEqual("cart", CartConfig.name)