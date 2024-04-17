from rest_framework.serializers import ModelSerializer
from todos.models import Todo
from authentication.serializers import GetUserDetailInTodo


class TodoRetrieveSerializer(ModelSerializer):

    owner = GetUserDetailInTodo(read_only=True)

    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "is_completed",
            "priority",
            "due_date",
            "description",
            "owner",
        ]


class TodoCreateSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "is_completed",
            "priority",
            "due_date",
            "description",
        ]
