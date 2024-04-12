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

        email = self.normalize_email(email)
        username = self.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin,TrackingModel):
    pass


