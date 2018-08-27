# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from models import Article


# Create your views here.

def articleView(request):
    return HttpResponse("rrr")
