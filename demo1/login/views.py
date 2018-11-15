from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse
from login.models import BookInfo, HeroInfo


# Create your views here.


def hello(req):
    return HttpResponse("hello world")

