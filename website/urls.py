# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<id>\d+)/$', views.article_detail, name="website_detail"),
    url(r'^home/', views.home, name="website_home"),
    url(r'^lv/', views.lv, name="website_test"),
]