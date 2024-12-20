from django.test import SimpleTestCase, RequestFactory
from unittest.mock import patch
from django.urls import reverse
from django.contrib.auth.models import User
from events.views import search_event_category

# Mock class to simulate EventCategory objects
class MockEventCategory:
    def __init__(self, name, code, status):
        self.name = name
        self.code = code
        self.status = status

class SearchEventCategoryTest(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('admin_events:search-event-category')

        # Create a mock user to simulate login
        self.user = User.objects.create_user(username='testuser', password='password')

    @patch('events.views.EventCategory.objects.filter')
    def test_search_event_category_view_with_results(self, mock_filter):
        # Mock the filter return value
        mock_filter.return_value = [
            MockEventCategory(name="Music Festival", code="MUSIC01", status="active")
        ]
        
        # Create a request and simulate user login
        request = self.factory.post(self.url, data={'search': 'Music'})
        request.user = self.user  # Manually set the user

        response = search_event_category(request)

        # Assert that the response is OK
        self.assertEqual(response.status_code, 200)
        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'events/event_category.html')
        # Assert that the context contains the mocked results
        self.assertIn('event_category', response.context)
        self.assertEqual(len(response.context['event_category']), 1)
        self.assertEqual(response.context['event_category'][0].name, "Music Festival")

    @patch('events.views.EventCategory.objects.filter')
    def test_search_event_category_view_without_results(self, mock_filter):
        # Mock the filter return value for no results
        mock_filter.return_value = []
        
        # Create a request and simulate user login
        request = self.factory.post(self.url, data={'search': 'Nonexistent'})
        request.user = self.user  # Manually set the user

        response = search_event_category(request)

        # Assert that the response is OK
        self.assertEqual(response.status_code, 200)
        # Assert that no results are found
        self.assertEqual(len(response.context['event_category']), 0)
