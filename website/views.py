# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render

from models import Article


# Create your views here.

def home(request):
    post_list = Article.objects.all()
    return render(request, 'website/home.html', {'post_list': post_list})


def lv(request):
    return render(request, 'website/test.html', {'current_time': datetime.now()})


def article_detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'website/post.html', {'post': post})
