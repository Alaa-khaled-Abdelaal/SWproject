from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import EventCategory

class EventCategoryUpdateViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create an EventCategory instance
        self.event_category = EventCategory.objects.create(name='Test Category', code='TEST', status='active')
        
        # Define the URL for the update view
        self.url = reverse('edit_event_category', args=[self.event_category.pk])

    def test_redirect_if_not_logged_in(self):
        # Test that a user is redirected to the login page if not logged in
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/login/?next={self.url}')

    def test_logged_in_user_can_access_edit_page(self):
        # Log in the test user
        self.client.login(username='testuser', password='password')
        
        # Get the response from the update page
        response = self.client.get(self.url)
        
        # Check that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)
        
        # Check if the form is populated with the EventCategory data
        self.assertContains(response, 'Test Category')
        self.assertContains(response, 'TEST')

    def test_form_submission_updates_event_category(self):
        # Log in the test user
        self.client.login(username='testuser', password='password')
        
        # Define the data to update the EventCategory
        data = {'name': 'Updated Category', 'code': 'UPDATED', 'status': 'inactive'}
        
        # Post the form with the updated data
        response = self.client.post(self.url, data)
        
        # Reload the EventCategory from the database
        self.event_category.refresh_from_db()
        
        # Check that the EventCategory was updated
        self.assertEqual(self.event_category.name, 'Updated Category')
        self.assertEqual(self.event_category.code, 'UPDATED')
        self.assertEqual(self.event_category.status, 'inactive')
        
        # Check that the user was redirected after submission
        self.assertRedirects(response, reverse('event_category_list'))  # Adjust this to your post-submit redirect URL
