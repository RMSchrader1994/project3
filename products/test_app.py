from django.apps import apps
from django.test import TestCase
from .apps import ProductsConfig

class TestAccountsConfig(TestCase):
    def test_products_app(self):
        self.assertEqual("products", ProductsConfig.name)