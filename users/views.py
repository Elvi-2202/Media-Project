from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer
from drf_spectacular.utils import extend_schema

class SignUpView(APIView):
    serializer_class = SignUpSerializer 
    permission_classes = [] 

    @extend_schema(
        request=SignUpSerializer,
        responses={201: dict, 400: dict}
    )
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Utilisateur créé avec succès."}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def users(request):
    return HttpResponse("Hello Users!!!")


# Create your views here.
