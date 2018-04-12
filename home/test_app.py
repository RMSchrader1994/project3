from django.apps import apps
from django.test import TestCase
from .apps import HomeConfig

class TestHomeConfig(TestCase):
    def test_home_app(self):
        self.assertEqual("home", HomeConfig.name)