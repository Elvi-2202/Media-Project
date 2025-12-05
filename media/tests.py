# media/tests.py
from django.test import TestCase
from .models import Media, MediaJob

class MediaTestCase(TestCase):
    def setUp(self):
        self.media = Media.objects.create(
            title='Titre test',
            video_url='https://example.com/video.mp4',  # ajout obligatoire
            thumbnail_url='https://example.com/thumb.jpg'  # facultatif
        )

    def test_media_creation(self):
        self.assertEqual(self.media.title, 'Titre test')

    def test_media_update(self):
        self.media.title = 'Titre modifié'
        self.media.save()
        self.assertEqual(Media.objects.get(id=self.media.id).title, 'Titre modifié')

    def test_media_delete(self):
        media_id = self.media.id
        self.media.delete()
        self.assertFalse(Media.objects.filter(id=media_id).exists())

class MediaJobTestCase(TestCase):
    def setUp(self):
        self.media = Media.objects.create(
            title='Titre test',
            video_url='https://example.com/video.mp4'
        )
        self.job = MediaJob.objects.create(media=self.media)

    def test_mediajob_creation(self):
        self.assertEqual(self.job.status, 'pending')

    def test_mediajob_update(self):
        self.job.status = 'done'
        self.job.save()
        self.assertEqual(MediaJob.objects.get(id=self.job.id).status, 'done')

    def test_mediajob_delete(self):
        job_id = self.job.id
        self.job.delete()
        self.assertFalse(MediaJob.objects.filter(id=job_id).exists())
