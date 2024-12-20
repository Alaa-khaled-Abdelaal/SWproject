from django.test import SimpleTestCase, RequestFactory
from django.urls import reverse
from events.views import search_event_category
from events.models import EventCategory

class SearchEventCategoryTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('admin_events:search-event-category')
        # Creating some EventCategory objects for testing
        EventCategory.objects.create(name="Music Festival", code="MUSIC01", status="active")
        EventCategory.objects.create(name="Art Exhibition", code="ART01", status="active")
        EventCategory.objects.create(name="Tech Conference", code="TECH01", status="inactive")

    def test_search_event_category_view_with_results(self):
        request = self.factory.post(self.url, data={'search': 'Music'})
        response = search_event_category(request)
        
        # Assert that the response is OK
        self.assertEqual(response.status_code, 200)
        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'events/event_category.html')
        # Assert that the context contains the filtered results
        self.assertIn('event_category', response.context_data)
        self.assertEqual(len(response.context_data['event_category']), 1)
        self.assertEqual(response.context_data['event_category'][0].name, "Music Festival")

    def test_search_event_category_view_without_results(self):
        request = self.factory.post(self.url, data={'search': 'Nonexistent'})
        response = search_event_category(request)
        
        # Assert that the response is OK
        self.assertEqual(response.status_code, 200)
        # Assert that no results are found
        self.assertEqual(len(response.context_data['event_category']), 0)
    
    def test_search_event_category_view_no_search(self):
        request = self.factory.get(self.url)
        response = search_event_category(request)

        # Assert that the response is OK
        self.assertEqual(response.status_code, 200)
        # Assert that no search query returns the unfiltered template
        self.assertNotIn('event_category', response.context_data)
