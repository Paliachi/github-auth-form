from django.test import TestCase, Client
from django.urls import reverse

from apps.accounts_app.models import Profile, Account
from apps.accounts_app.forms import ProfileForm


class AccountProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile')
        self.user = Account.objects.create_user(
            username='Test',
            password='Test123!@#'
        )

    def test_profile_GET_not_logged_in(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 302)

    def test_profile_GET_logged_in(self):
        self.client.login(
            username='Test',
            password='Test123!@#'
        )
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_profile.html')


class ProfileFormViewTest(TestCase):
    """Tests profile form view"""
    def setUp(self):
        self.client = Client()
        self.user = Account.objects.create_user(
            username='Test2',
            password='Test123!@#2'
        )
        self.profile = Profile.objects.get(user=self.user)
        self.profile_form_url = reverse('profileForm')

    def test_profile_form_GET_not_logged_in(self):
        response = self.client.get(self.profile_form_url)

        self.assertEquals(response.status_code, 302)

    def test_profile_form_GET_logged_in(self):
        self.client.login(
            username='Test2',
            password='Test123!@#2'
        )
        response = self.client.get(self.profile_form_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_form.html')

    def test_validate_form_POST_update(self):
        data = {
            'full_name': 'Test Tester',
            'past_address': 'Past address',
            'current_address': 'Current address'
        }

        form = ProfileForm(
            data=data,
            instance=self.profile
        )
        form.save()
        response = self.client.post(self.profile_form_url)

        self.assertTrue(form.is_valid())
        self.assertEquals(response.status_code, 302)

    def test_validate_form_POST_partial_update(self):
        data = {
            'past_address': 'New Past address',
            'current_address': 'New Current address'
        }

        form = ProfileForm(
            data=data,
            instance=self.profile
        )
        form.save()
        response = self.client.post(self.profile_form_url)
        updated_instance = Profile.objects.get(user=self.user)

        self.assertTrue(form.is_valid())
        self.assertEquals(response.status_code, 302)
        self.assertEquals(updated_instance.past_address, 'New Past address')


class GithubLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = Account.objects.create_user(
            username='tester13',
            password='Test1234!@',
        )

    def test_login(self):
        response = self.client.post(self.login_url)
        sign_in = self.client.login(
            username='tester13',
            password='Test1234!@'
        )

        self.assertTrue(sign_in)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'github_login.html')


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('logout')
        self.user = Account.objects.create_user(
            username='tester13',
            password='Test1234!@',
        )

    def test_logout(self):
        response = self.client.get(self.logout_url)
        sign_in = self.client.login(
            username='tester13',
            password='Test1234!@'
        )
        self.assertTrue(sign_in)
        self.client.logout()
        self.assertEquals(response.status_code, 302)


class DeleteUserViewTest(TestCase):
    def test_delete_user_POST(self):
        client = Client()
        delete_url = reverse('deleteUser')
        Account.objects.create_user(
            username='tester131',
            password='Test1234!@4',
        )
        client.login(
            username='tester131',
            password='Test1234!@4'
        )
        response = client.post(delete_url)

        self.assertEquals(response.status_code, 302)








