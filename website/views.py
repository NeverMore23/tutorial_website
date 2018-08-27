# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from models import Article


# Create your views here.

def articleView(request):
    obj = Article.objects.all()
    obj_list = []
    for temp in obj:
        obj_list.append(temp.title)
    return render(request, 'website/index.html', {'current_time': datetime.now()})
