from django.contrib import admin
from .models import CustomUser, Profile, Post, Comment, Like, Dislike, FollowRelation
from django.contrib.auth.admin import UserAdmin


class UserConfig(UserAdmin):
    ordering = ('id',)

    list_display = ('id', 'email', 'username', 'is_active', 'gender', 'birthday')


# Register your models here.

admin.site.register(CustomUser, UserConfig)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(FollowRelation)