from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Todo List API",
        default_version="v1",
        description="API for managing todo items",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="anari.p62@gmail.com", version="1.0.0"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("authentication.urls")),
    path("api/todos/", include("todos.urls")),
]
