from django.shortcuts import render
from django.http import HttpResponse


def ping(request):
    return HttpResponse("pong")


def version(request):
    return HttpResponse("django_version")


# Create your views here.
