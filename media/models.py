from django.db import models

class Upload(models.Model):
    file_name = models.CharField(max_length=255)
    url = models.URLField()

# Create your models here.
