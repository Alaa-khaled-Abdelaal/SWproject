from django.test import TestCase
from django.contrib.auth.models import User
from events.models import EventCategory  # Adjust the import path as needed

class EventCategoryTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test EventCategory instance
        self.event_category = EventCategory.objects.create(
            name='Test Category',
            code='TEST',
            status='active',
            created_user=self.user,  # Add created_user
            updated_user=self.user   # Add updated_user to fix the NOT NULL constraint error
        )

    def test_event_category_creation(self):
        # Example test to verify the EventCategory instance is created
        self.assertEqual(self.event_category.name, 'Test Category')
        self.assertEqual(self.event_category.created_user, self.user)
        self.assertEqual(self.event_category.updated_user, self.user)
