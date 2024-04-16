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
