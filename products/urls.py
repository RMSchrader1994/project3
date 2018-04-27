from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from .views import *


urlpatterns = [
	url(r'^$', get_dlc, name="get_dlc"),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]