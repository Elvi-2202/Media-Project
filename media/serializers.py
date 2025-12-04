from django.conf import settings
from rest_framework import serializers

class ImageKitUploadSerializer(serializers.Serializer):
    public_key = settings.IMAGEKIT_PRIVATE_KEY
    private_key = settings.IMAGEKIT_PUBLIC_KEY
    url_endpoint = serializers.URLField(
        default="https://upload.imagekit.io/api/v1/files/upload",
    )
    file = serializers.ImageField() 