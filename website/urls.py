# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<id>\d+)/$', views.article_detail, name="article_detail"),
    url(r'^home/', views.home, name="home"),
    url(r'^lv/', views.lv, name="lv"),
]