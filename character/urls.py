from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', character_list, name='character_list'),
    url(r'^create/', create_characters, name='create_characters'),
    url(r'delete/(\d+)$', delete_character, name="delete_character"),
    url(r'edit/(\d+)$', edit_character, name="edit_character"),
    url(r'^characters/(\d+)', character_detail, name='character_detail'),
    ]