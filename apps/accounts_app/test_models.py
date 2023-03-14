from django.test import TestCase

from .models import Account, Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        user = Account.objects.create_user(
            username='tester',
            email='tester@tester.com',
            password='Testing123!@#'
        )
        Profile.objects.create(
            user=user,
            full_name="Test Test",
            past_address='Past 10',
            current_address='Current 10',
        )

    def test_profile_model(self):
        """Animals that can speak are correctly identified"""
        user = Account.objects.get(username='tester')
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.user.username, 'tester')
