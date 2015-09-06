__author__ = 'awemulya'

from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
                       url(r'^home/$', views.home, name='home'),
                       )