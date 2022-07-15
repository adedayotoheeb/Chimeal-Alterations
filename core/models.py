from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionManager
# Create your models here.

class User(AbstractBaseUser, PermissionManager):
    pass


