from rest_framework.authentication import get_authorization_header, BaseAuthentication
from authentication.models import User
from rest_framework import exceptions
from django.conf import settings
import jwt



class JWTAuthentication(BaseAuthentication):
    
     def authenticate(self, request):
        
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf_8')
        auth_token = auth_data(' ')

        
