from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView, status

class Ping(APIView):
    @extend_schema(
        summary="ping",
        description="Check the API is alive or not",
        responses={"200": PingSerializer},
        tags=["core"],
    )
    def get(self, request):
        return Response({"message": "pong"})

class Version(APIView):
    @extend_schema(
        summary="version",
        description="Check the API is alive or not",
        responses={"200": VersionSerializer},
        tags=["core"],
    )    
    def get(self, request):
        return Response({"version": "1.0.0"}) 


# Create your views here.
