from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from todos.models import Todo


class TodosAPITestCase(APITestCase):

    def create_todo(self):
        sample_todo = {
            "title": "title test",
            "description": "description test",
            "priority": "H",
            "is_completed": False,
            "due_date": "2022-12-12",
        }
        response = self.client.post(reverse("todos"), sample_todo)
        return response

    def authenticate(self):
        self.client.post(
            reverse("register"),
            {
                "username": "test",
                "first_name": "user",
                "last_name": "users",
                "email": "email@gmail.com",
                "password": "test",
            },
        )
        response = self.client.post(
            reverse("login"),
            {
                "username": "test",
                "password": "test",
            },
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")


class TestListCreateTodo(TodosAPITestCase):

    def test_should_not_create_todo_with_no_auth(self):
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
