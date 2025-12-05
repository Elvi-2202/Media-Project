from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        
        self.profile = UserProfile.objects.create(user=self.user, role='viewer')

    def test_userprofile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.role, 'viewer')

    def test_userprofile_update(self):
        self.profile.role = 'operator'
        self.profile.save()
        updated_profile = UserProfile.objects.get(id=self.profile.id)
        self.assertEqual(updated_profile.role, 'operator')

    def test_userprofile_delete(self):
        profile_id = self.profile.id
        self.profile.delete()
        self.assertFalse(UserProfile.objects.filter(id=profile_id).exists())
