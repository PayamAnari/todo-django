from django.urls import path
from todos.views import CreateTodoAPIView, TodoListAPIView


urlpatterns = [path("create", CreateTodoAPIView.as_view(), name="create_todo")
    path("list", TodoListAPIView.as_view(), name="list_todo")
]
