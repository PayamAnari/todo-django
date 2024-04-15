from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Todo
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated


class CreateTodoAPIView(CreateAPIView):
    serializer_class = TodoSerializer
    permission_class = [IsAuthenticated]
