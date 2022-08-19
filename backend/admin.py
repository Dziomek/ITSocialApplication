from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserConfig(UserAdmin):
    ordering = ('id',)

    list_display = ('id', 'email', 'username', 'is_active', 'gender', 'birthday')


# Register your models here.

admin.site.register(CustomUser, UserConfig)
