from django.test import TestCase
from .models import Upload

class MediaModelsTest(TestCase):
    def test_create_upload(self):
        upload = Upload.objects.create(file_name="image.jpg", url="http://example.com/image.jpg")
        self.assertEqual(upload.file_name, "image.jpg")
        self.assertEqual(upload.url, "http://example.com/image.jpg")
