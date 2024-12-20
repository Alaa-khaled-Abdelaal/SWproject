from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import EventCategory

class EventCategoryTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Log the user in
        self.client.login(username='testuser', password='testpassword')

        # Create a test event category
        self.category = EventCategory.objects.create(
            name="Test Category", code="TC01", status="active", 
            created_user=self.user, updated_user=self.user
        )

    def test_event_category_creation(self):
        # Create an EventCategory with both created_user and updated_user
        category = EventCategory.objects.create(
            name="Test Category", 
            code="TC01", 
            status="active", 
            created_user=self.user,  # Provide the user for created_user field
            updated_user=self.user   # Provide the user for updated_user field
        )
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.code, "TC01")
        self.assertEqual(category.created_user, self.user)
        self.assertEqual(category.updated_user, self.user)

    def test_event_category_list_view(self):
        # Send GET request to the event category list view
        response = self.client.get(reverse('admin_events:event-category-list'))
        
        # Print the response content for debugging
        print(response.content)
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Assert that the text "Test Category" is in the response
        self.assertContains(response, "Test Category")
