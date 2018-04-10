from django.test import TestCase
from django.urls import resolve
from .views import *

# Create your tests here.
class TestAccounts(TestCase):
    def test_login_url_returns_ok(self):
        response = self.client.get("/accounts/login")
        self.assertEqual(response.status_code, 200)
    def test_login_url_returns_view(self):
        found = resolve('/accounts/login')
        self.assertEqual(found.func, login)
        
    def test_register_url_returns_ok(self):
        response = self.client.get("/accounts/register")
        self.assertEqual(response.status_code, 200)
    def test_register_url_returns_view(self):
        found = resolve('/accounts/register')
        self.assertEqual(found.func, register)
        
    
    
    
    