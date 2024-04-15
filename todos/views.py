from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Todo
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated


class TodosListAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class CreateTodoAPIView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_class = [
#         IsAuthenticated,
#     ]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class TodoListAPIView(ListAPIView):
#     serializer_class = TodoSerializer
#     permission_class = [
#         IsAuthenticated,
#     ]

#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)
