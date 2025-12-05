from django.test import TestCase
from .models import Ping, Version

class PingTestCase(TestCase):
    def test_ping_creation(self):
        ping = Ping.objects.create(message="pong")
        self.assertEqual(ping.message, "pong")

class VersionTestCase(TestCase):
    def test_version_creation(self):
        version = Version.objects.create(version="1.0.0")
        self.assertEqual(version.version, "1.0.0")
