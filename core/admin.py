from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
# Register your models here.


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'username', 'first_name',
                'last_name', 'is_active', 'is_superuser', 'is_staff']
    ordering = ['email', 'username', 'first_name',
                'last_name', 'is_active', 'is_superuser', 'is_staff']
