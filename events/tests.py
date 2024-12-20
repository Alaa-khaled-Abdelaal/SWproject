from django.contrib.auth.models import User
from django.test import TestCase
from .models import EventCategory

class EventCategoryTests(TestCase):

    def setUp(self):
        # Create a user for both created_user and updated_user fields
        self.user = User.objects.create_user(username="testuser", password="testpassword")

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
        # Authenticate the user before accessing the view
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('admin_events:event-category-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")
