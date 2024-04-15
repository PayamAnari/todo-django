from django.urls import path
from todos.views import TodosAPIView, TodoDetailAPIView


urlpatterns = [
    path("", TodosAPIView.as_view(), name="todos"),
    path("<int:id>", TodoDetailAPIView.as_view(), name="detail_todos"),
    # path("create", CreateTodoAPIView.as_view(), name="create_todo"),
    # path("list", TodoListAPIView.as_view(), name="list_todos"),
]
