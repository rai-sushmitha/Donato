from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	# /donator/
    url(r'^$', views.index, name='index'),
    # /donator/321/
    url(r'^(?P<donation_id>[0-9]+)/$', views.detail, name='details')
]