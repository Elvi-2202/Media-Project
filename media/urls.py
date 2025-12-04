from django.urls import path
from .views import UploadView

urlpatterns = [
    path("upload/", UploadView, name="upload-file")
]