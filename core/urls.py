from django.urls import path
from .views import Ping
from .views import Version


urlpatterns = [
    path("version", Version.as_view(), name="version"),
    path("ping", Ping.as_view(), name="ping"),
   
]
