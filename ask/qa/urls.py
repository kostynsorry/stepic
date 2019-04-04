# -*- coding: utf-8 -*-

from django.urls import re_path, path
from . import views

urlpatterns = [
    # re_path(r'^$', views.test, name='index'),
    # re_path(r'^signup/', views.test, name='signup'),
    # re_path(r'^login/', views.test, name='login'),
    # re_path(r'^questions/\d+/', views.test, name='questions'),
    # re_path(r'^ask/', views.test, name='ask'),
    # re_path(r'^popular/', views.test, name='popular'),
    # re_path(r'^new/', views.test, name='new')

    # path('', views.test, name='index'),
    path('signup/', views.test, name='signup'),
    path('login/', views.test, name='login'),
    path('questions/<int:index>', views.detail, name='questions'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.test, name='new'),
    path('', views.main, name='main')
]
