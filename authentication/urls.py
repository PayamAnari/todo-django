from authentication import views
from django.urls import path


urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('users', views.UsersAPIView.as_view(), name='users'),
]