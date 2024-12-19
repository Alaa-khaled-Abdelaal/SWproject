from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from events.models import Payments, Event

class UserViewsTest(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = Client()

        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
            first_name="Test",
            last_name="User"
        )

        # Create test event and payment data
        self.event = Event.objects.create(name="Test Event")
        Payments.objects.create(username=self.user.username, eventName=self.event.name)

    def test_register_user_success(self):
        response = self.client.post(reverse('useracc:register'), {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_user_password_mismatch(self):
        response = self.client.post(reverse('useracc:register'), {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'password123',
            'password2': 'password456',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Password not matching")

    def test_login_user_success(self):
        response = self.client.post(reverse('useracc:login'), {
            'email': 'testuser@example.com',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success

    def test_logout_user(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('useracc:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect on logout

    def test_profile_user_update(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('useracc:Yourprofile'), {
            'first_name': 'Updated',
            'last_name': 'User',
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 200)
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.first_name, 'Updated')
        self.assertEqual(updated_user.username, 'updateduser')
