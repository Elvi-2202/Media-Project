import base64
import requests
from django.conf import settings

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Upload image",
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "file": {"type": "string", "format": "binary"}
            },
            "required": ["file"]
        }
    },
    responses={200: dict},
)
@api_view(["POST"])
@parser_classes([MultiPartParser])
def UploadView(request):

    file = request.FILES.get("file")

    auth = base64.b64encode(f"{settings.IMAGEKIT_PRIVATE_KEY}:".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}


    files = {"file": (file.name, file.read())}
    data = {"fileName": file.name}

  
    response = requests.post(
            "https://upload.imagekit.io/api/v1/files/upload",
            headers=headers,
            files=files,
            data=data
    )
    return Response(response)