from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (AbstractBaseUser,UserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _



class MyUserManager(UserManager):
    
    def _create_user(self, username, email, password, **extra_fields):
        
        if not username:
            raise ValueError('The given username must be set')
        
        if not email:
            raise ValueError('The given email must be set')

class User(AbstractBaseUser,PermissionsMixin,TrackingModel):
    pass


