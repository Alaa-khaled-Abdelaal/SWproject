from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import EventCategory

class EventCategoryTests(TestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        # Create an EventCategory for the list view
        self.category = EventCategory.objects.create(
            name="Test Category", 
            code="TC01", 
            status="active", 
            created_user=self.user
        )

    def test_event_category_list_view(self):
        # Authenticate the user before accessing the view
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('admin_events:event-category-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")
