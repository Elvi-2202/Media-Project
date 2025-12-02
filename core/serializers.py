from rest_framework import serializers


class PingSerializer(serializers.Serializer):
    response = serializers.CharField()
class VersionSerializer(serializers.Serializer):
    response = serializers.CharField()
  