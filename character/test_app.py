from django.apps import apps
from django.test import TestCase
from .apps import CharacterConfig

class TestAccountsConfig(TestCase):
    def test_character_app(self):
        self.assertEqual("character", CharacterConfig.name)