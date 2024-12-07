# projects/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Project


class PledgeTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.project = Project.objects.create(
            title='Test Project',
            description='A project for testing',
            goal=1000,
            image='http://example.com/image.jpg',
            is_open=True,
            current_funded_amount=0,
            owner=self.user
        )
        self.client.login(username='testuser', password='testpass')

    def test_create_pledge(self):
        data = {
            'amount': 50,
            'comment': 'Test pledge',
            'anonymous': False,
            'project': self.project.id
        }
        response = self.client.post('/pledges/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['amount'], 50)
        self.assertEqual(response.data['supporter'], self.user.id)

