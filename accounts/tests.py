from django.test import TestCase
from django.urls import resolve
from .views import *
from .forms import *
from django import forms
from django.conf import settings

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
        
        
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'adminadmin!',
            'password2': 'adminadmin!',
        })
 
        self.assertTrue(form.is_valid())
        
    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'password1': 'adminadmin!',
            'password2': 'adminadmin!',
        })
 
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())
    
    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'adminadmin!',
            'password2': 'adminadmin1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())
                                 
    def test_forms_register_with_duplicate_email(self):
        self.user = User.objects.create_user(username='user', password='password', email="user@example.com")
        details = {
            'username': 'a_different_user',
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password'
        }
        response = self.client.post("/accounts/register", details)
        self.assertFormError(response, 'form', 'email', 'Email addresses must be unique.')
        
        
        
                                 
   
        
        
    
    
    
    