import base64
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser 
from drf_spectacular.utils import extend_schema
from .serializers import ImageKitUploadSerializer


class UploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    @extend_schema(
        request=ImageKitUploadSerializer,
        tags=["media"],
        responses={200: dict, 400: dict, 500: dict}
    )
    def post(self, request):
        serializer = ImageKitUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        private_key = data["private_key"]
        upload_endpoint = data.get("url_endpoint", "https://upload.imagekit.io/api/v1/files/upload")

        auth = base64.b64encode(f"{private_key}:".encode()).decode()
        headers = {"Authorization": f"Basic {auth}"}
        
        payload = {} 
        files = {}
        
        if data.get('file'):
            uploaded_file = data['file']
            files = {"file": (uploaded_file.name, uploaded_file.read())}
            payload["fileName"] = uploaded_file.name
            
        elif data.get('media_url'):
            media_url = data['media_url']
            payload["file"] = media_url
            
            try:
                file_name = media_url.split('/')[-1].split('?')[0]
                payload["fileName"] = file_name if file_name else "remote_upload"
            except:
                payload["fileName"] = "remote_upload"
        
        try:
            response = requests.post(
                upload_endpoint,
                headers=headers,
                files=files,  
                data=payload,
            )

            return Response(response.json(), status=response.status_code)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": f"Erreur de connexion lors de l'upload: {str(e)}"},
                status=500
            )