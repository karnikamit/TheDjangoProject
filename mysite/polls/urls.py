# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from django.conf.urls import url
from . import views
urlpatterns = [url(r'^$', views.index, name='index'),  # ex: /polls
               url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),  # ex: /polls/3
               url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),   # ex:/polls/3/results
               url(r'^(?P<question_id>[0-9]+)/votes/$', views.vote, name='vote')]   # ex: /polls/3/votes
