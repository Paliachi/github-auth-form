from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import Profile, Account


class AccountProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile')
        self.user = Account.objects.create_user(username='Test', password='Test123!@#')

    def test_profile_GET_not_logged_in(self):
        response = self.client.get(self.profile_url)
        request = self.client.request()

        self.assertEquals(response.status_code, 302)
        self.assertEquals(request.status_code, 404)

    def test_profile_GET_logged_in(self):
        self.client.login(username='Test', password='Test123!@#')
        response = self.client.get(reverse('profile'))

        self.assertEquals( response.status_code, 200)
        self.assertTemplateUsed(response, 'account_profile.html')


class ProfileFormViewTest(TestCase):
    def setUp(self):
        self.client = Client()

