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
    
    # # 測試 create
    # def test_create_todo(self):
    #     data = {'title': 'Learn DRF'}
    #     response = self.client.post(self.base_url, data, format='json', **self.auth_headers)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertTrue(response.data['title'].startswith('Learn DRF'))

    # # 測試 authentication
    # def test_get_todos_autheticated(self):
    #     Todo.objects.create(title='Item 1', kind='abcd')
    #     response = self.client.get(self.base_url, **self.auth_headers)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIsInstance(response.data, list)
    #     self.assertGreaterEqual(len(response.data), 1)

    # # 反向測試 unauthentication
    # def test_get_todos_unauthenticated(self):
    #     response = self.client.get(self.base_url)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # # 帶 queryString 測試
    # def test_filter_todos_by_title(self):
    #     Todo.objects.create(title='Homework')
    #     Todo.objects.create(title='Buy groceries')
    #     response = self.client.get(f'{self.base_url}?title=Homework', **self.auth_headers)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['title'], 'Homework')

    # def test_create_invalid_todo(self):
    #     data = {'title': ""}
    #     response = self.client.post(self.base_url, data, format='json', **self.auth_headers)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 測試 patch
    # def test_patch_todos_by_title(self):
    #     # 建立一個 Todo 實例
    #     todo = Todo.objects.create(title='abc123')
        
    #     # 定義更新資料
    #     data = {'title': 'alex-test'}
    #     print(data)
        
    #     # 更新特定 Todo
    #     response = self.client.patch(f'{self.base_url}/{todo.id}', data, format='json', **self.auth_headers)
        
    #     # 驗證回應
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['title'], 'alex-test')

    def test_delete_todo(self):
        # 建立一個 Todo 實例
        todo = Todo.objects.create(title='abc123')
        
        # 發送 DELETE 請求
        response = self.client.delete(f'{self.base_url}/{todo.id}', **self.auth_headers)
        
        # 驗證回應
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)