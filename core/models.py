from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, username, last_name, phone_number,password, **other_fields):
        """Create a new user from the given email and password."""
        if not email:
            raise ValueError("Please enter an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, username=username,
                          last_name=last_name, phone_number=phone_number,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, password,phone_number, **other_fields):
        """Create a new superuser"""
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(' Superuser must be assigned to is_staff = True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                ' Superuser must be assigned to is_superuser = True.')

        return self.create_user(email, username, first_name, last_name,phone_number, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', "phone_number"]

    objects: BaseUserManager = UserManager()

    def __str__(self) -> str:
        return self.email
