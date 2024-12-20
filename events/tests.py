from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from events.models import Event, EventUserWishList, EventCategory, JobCategory, Ticket
from django.utils import timezone

class RemoveEventUserWishDeleteViewTest(TestCase):
    
    def setUp(self):
        # Create user and authenticate them
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create Event and related objects
        category = EventCategory.objects.create(name="Test Category", code="TST001", created_user=self.user, updated_user=self.user, status='active')
        job_category = JobCategory.objects.create(name="Test Job Category")
        event = Event.objects.create(category=category, name="Test Event", job_category=job_category, scheduled_status="scheduled", venue="Test Venue", start_date=timezone.now(), end_date=timezone.now(), location="Point(10 10)", maximum_attende=100, created_user=self.user, updated_user=self.user, status='active', price=50.00)

        # Create a wish list item for the event
        self.event_wish = EventUserWishList.objects.create(user=self.user, event=event, created_user=self.user, updated_user=self.user, status='active')

        # URL for removing the event wish
        self.url = reverse('admin_events:remove-event-user-wish', kwargs={'pk': self.event_wish.pk})

    def test_redirect_if_not_logged_in(self):
        # Check that the user is redirected to login if they are not logged in
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/login/?next={self.url}')

    def test_delete_event_wish_success(self):
        # Log in the user
        self.client.login(username='testuser', password='password')

        # Ensure the wish list item exists before deletion
        self.assertEqual(EventUserWishList.objects.count(), 1)

        # Make a POST request to the delete view
        response = self.client.post(self.url)

        # Assert that the user is redirected to the success URL
        self.assertRedirects(response, reverse('admin_events:event-wish-list'))

        # Ensure that the EventUserWishList object is deleted
        with self.assertRaises(EventUserWishList.DoesNotExist):
            EventUserWishList.objects.get(pk=self.event_wish.pk)

    def test_object_not_found(self):
        # Log in the user
        self.client.login(username='testuser', password='password')

        # Try to delete a non-existing object (non-existing PK)
        non_existing_url = reverse('admin_events:remove-event-user-wish', kwargs={'pk': 9999})
        
        # Assert that a 404 error is raised
        response = self.client.post(non_existing_url)
        self.assertEqual(response.status_code, 404)
