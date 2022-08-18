from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserConfig(UserAdmin):
    list_display = ('id', 'email', 'username', 'is_active')


# Register your models here.

admin.site.register(CustomUser, UserConfig)
