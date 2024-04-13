from authentication import views
from django.urls import path


urlpatterns = [
    path('register', views.RegisterAPIViews.as_view(), name-'register'),
]