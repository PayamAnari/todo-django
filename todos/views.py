from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from todos.serializers import (
    TodoRetrieveSerializer,
    TodoCreateSerializer,
)
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from todos.pagination import CustomPageNumberPagination


class TodosAPIView(ListCreateAPIView):
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["id", "title", "is_completed", "priority", "due_date"]
    search_fields = ["title", "description", "priority", "is_completed"]
    ordering_fields = ["id", "created_at", "due_date", "priority", "is_completed"]

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TodoRetrieveSerializer
        elif self.request.method == "POST":
            return TodoCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TodoRetrieveSerializer
        elif self.request.method in ["PUT", "PATCH", "DELETE"]:
            return TodoCreateSerializer


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
