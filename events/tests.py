from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from events.models import EventUserWishList
from django.http import Http404

class RemoveEventUserWishDeleteViewTest(TestCase):
    
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create an EventUserWishList object for the user
        self.event_wish = EventUserWishList.objects.create(user=self.user, event_name="Test Event", event_code="TEST001")

        # URL for deleting the EventUserWishList
        self.url = reverse('admin_events:remove_event_user_wish', kwargs={'pk': self.event_wish.pk})

    def test_redirect_if_not_logged_in(self):
        # Check that the user is redirected to login if they are not logged in
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/login/?next={self.url}')

    def test_delete_event_wish_success(self):
        # Log in the user
        self.client.login(username='testuser', password='password')

        # Make a GET request to the delete view (this triggers the deletion)
        response = self.client.post(self.url)  # POST is typically used for delete actions

        # Assert that the user is redirected to the success URL
        self.assertRedirects(response, reverse('admin_events:event-wish-list'))

        # Assert that the EventUserWishList object no longer exists
        with self.assertRaises(EventUserWishList.DoesNotExist):
            EventUserWishList.objects.get(pk=self.event_wish.pk)

    def test_object_not_found(self):
        # Log in the user
        self.client.login(username='testuser', password='password')

        # Try to delete a non-existing object
        non_existing_url = reverse('admin_events:remove_event_user_wish', kwargs={'pk': 9999})
        
        # Assert that a 404 error is raised
        response = self.client.post(non_existing_url)
        self.assertEqual(response.status_code, 404)

