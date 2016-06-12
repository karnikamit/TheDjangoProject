# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from django.conf.urls import url
from . import views
urlpatterns = [url(r'^$', views.index, name='index')]
