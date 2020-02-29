from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	# /login/
    url(r'^$', views.index, name='index')
]