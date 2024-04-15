from authentication import views
from django.urls import path


urlpatterns = [
    path("register", views.RegisterAPIView.as_view(), name="register"),
    path("users", views.UsersAPIView.as_view(), name="users"),
    path("users/<int:pk>", views.UserAPIView.as_view(), name="user"),
    path("login", views.LoginAPIView.as_view(), name="login"),
    path("logout", views.LogOutAPIView.as_view(), name="logout"),
    path("user", views.AuthUserAPIView.as_view(), name="user"),
    path("user/<int:pk>/", views.DeleteUserAPIView.as_view(), name="delete-user"),
    path(
        "user/<int:pk>/update/", views.UpdateUserAPIView.as_view(), name="update-user"
    ),
]
