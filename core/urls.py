from django.urls import path
from . import views

urlpatterns = [
    path("version", views.version, name="version"),
    path("ping", views.ping, name="ping"),
]
