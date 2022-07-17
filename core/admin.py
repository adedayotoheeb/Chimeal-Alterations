from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
# Register your models here.

@admin.register(models.User)
class UserAdmin(BaseUserAdmin): 
    list_display =  ['user_name', 'email', 'first_name', 'last_name']
    ordering = ['email', 'user_name','first_name', 'last_name', 'is_active', 'is_superuser','is_staff']  
    fieldsets = (
        (None, {"fields": ("user_name", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )



