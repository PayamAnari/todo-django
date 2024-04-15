from django.urls import path
from todos.views import TodosListAPIView


urlpatterns = [
    path("", TodosListAPIView.as_view(), name="list_todos")
    # path("create", CreateTodoAPIView.as_view(), name="create_todo"),
    # path("list", TodoListAPIView.as_view(), name="list_todos"),
]
