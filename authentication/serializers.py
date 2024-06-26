from rest_framework import serializers
from authentication.models import User


class RegisterSerializers(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "token"]

        read_only_fields = ["token"]


class UpdateUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "is_superuser",
        ]


class GetUserDetailInTodo(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserDetailSerializer(serializers.ModelSerializer):
    todo_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "is_superuser",
            "created_at",
            "email_verified",
            "todo_count",
        ]

    def get_todo_count(self, obj):
        return obj.get_todo_count()
