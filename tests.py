from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse

class NotificationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('notification')

    def test_success_message(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].level, messages.SUCCESS)
        self.assertEqual(messages[0].message, 'This is a success message.')

    def test_error_message(self):
        # Simulate the error condition
        with self.settings(ERROR_CONDITION=True):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            messages = list(response.context['messages'])
            self.assertEqual(len(messages), 1)
            self.assertEqual(messages[0].level, messages.ERROR)
            self.assertEqual(messages[0].message, 'This is an error message.')
# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User, Group
# from django.contrib.auth import get_user_model

# class AuthorizationTests(TestCase):
#     def setUp(self):
#         self.client = Client()
        
#         self.organizer_group = Group.objects.create(name='organizer')
#         self.participant_group = Group.objects.create(name='participant')

#         self.organizer_user = get_user_model().objects.create_user(username='organizer', password='password')
#         self.participant_user = get_user_model().objects.create_user(username='participant', password='password')
#         self.other_user = get_user_model().objects.create_user(username='other', password='password')

#         self.organizer_user.groups.add(self.organizer_group)
#         self.participant_user.groups.add(self.participant_group)

#     def test_organizer_view_access(self):
#         self.client.login(username='organizer', password='password')
#         response = self.client.get(reverse('organizer_view'))
#         self.assertEqual(response.status_code, 200)

#         self.client.login(username='participant', password='password')
#         response = self.client.get(reverse('organizer_view'))
#         self.assertEqual(response.status_code, 403)

#     def test_participant_view_access(self):
#         self.client.login(username='participant', password='password')
#         response = self.client.get(reverse('participant_view'))
#         self.assertEqual(response.status_code, 200)

#         self.client.login(username='organizer', password='password')
#         response = self.client.get(reverse('participant_view'))
#         self.assertEqual(response.status_code, 403)


