from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Todo
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TodosListAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return Response(
            {"message": "Todo created successfully"}, status=status.HTTP_201_CREATED
        )


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
