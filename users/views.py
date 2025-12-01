from django.shortcuts import render
from django.http import HttpResponse


def users(request):
    return HttpResponse("Hello Users!!!")


# Create your views here.
