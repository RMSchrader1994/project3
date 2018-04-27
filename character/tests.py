from django.test import TestCase
from django.urls import resolve
from .views import *

# Create your tests here.
class TestAccounts(TestCase):
    def test_create_url_returns_ok(self):
        response = self.client.get("/character/create/")
        self.assertEqual(response.status_code, 302)
    def test_create_url_returns_view(self):
        found = resolve("/character/create/")
        self.assertEqual(found.func, create_characters)
        
    def test_character_list_url_returns_ok(self):
        response = self.client.get("/character/")
        self.assertEqual(response.status_code, 302)
    def test_character_list_url_returns_view(self):
        found = resolve("/character/")
        self.assertEqual(found.func, character_list)
        
    
    def test_edit_url_returns_view(self):
        found = resolve("/character/edit/2")
        self.assertEqual(found.func, edit_character)
        
    
    def test_delete_url_returns_view(self):
        found = resolve("/character/delete/10")
        self.assertEqual(found.func, delete_character)
        
    
    def test_character_info_url_returns_view(self):
        found = resolve("/character/10")
        self.assertEqual(found.func, character_detail)