# This file is for Unit Test.

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Todo
from rest_framework_simplejwt.tokens import RefreshToken

class TodoAPITestCase(APITestCase):
    # Create fake data, prepare for testing
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = self.get_access_token(self.user)
        self.auth_headers = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        self.base_url = '/api/todos'

    def get_access_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
    def test_create_todo(self):
        data = {'title': 'Learn DRF'}
        response = self.client.post(self.base_url, data, format='json', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['title'].startswith('Learn DRF'))