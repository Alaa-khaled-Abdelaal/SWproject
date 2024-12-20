

from django.test import TestCase
from django.urls import reverse
from .models import EventCategory

class EventCategoryTests(TestCase):

    def test_event_category_creation(self):
        category = EventCategory.objects.create(name="Test Category", code="TC01", status="active")
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.code, "TC01")

    def test_event_category_list_view(self):
        response = self.client.get(reverse('admin_events:event-category-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")

