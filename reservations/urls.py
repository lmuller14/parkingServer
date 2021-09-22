from django.urls import path
from django.conf.urls import url
from reservations.views import user_collection, user_element

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'users/$', user_collection, name='user_collection'),
    url(r'users/(?P<pk>[0-9]+)$', user_element, name='user_element'),
]