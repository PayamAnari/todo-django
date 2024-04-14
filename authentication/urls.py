from authentication import views
from django.urls import path


urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('users', views.UsersAPIView.as_view(), name='users'),
    path('users/<int:pk>', views.UserAPIView.as_view(), name='user'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('user', views.AuthUserAPIView.as_view(), name='user'),
]