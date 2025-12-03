from rest_framework import serializers

class ImageKitUploadSerializer(serializers.Serializer):
    public_key = serializers.CharField( 
    )
    private_key = serializers.CharField(
    )
    url_endpoint = serializers.URLField(
        default="https://upload.imagekit.io/api/v1/files/upload",
    )
    media_url = serializers.URLField(
    )
