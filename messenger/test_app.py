from django.apps import apps
from django.test import TestCase
from .apps import MessengerConfig

class TestAccountsConfig(TestCase):
    def test_messanger_app(self):
        self.assertEqual("messenger", MessengerConfig.name)