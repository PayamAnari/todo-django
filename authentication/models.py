from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

class User(AbstractBaseUser,PermissionsMixin,TrackingModel):
    pass


