from django.contrib import admin
from .models import CustomUser, Profile, Post, Comment, Like, Dislike, FollowRelation, Notification, Message
from django.contrib.auth.admin import UserAdmin


class UserConfig(UserAdmin):
    ordering = ('id',)

    list_display = ('id', 'email', 'username', 'is_active', 'gender', 'birthday', 'profile_img')


# Register your models here.

admin.site.register(CustomUser, UserConfig)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(FollowRelation)
admin.site.register(Notification)
admin.site.register(Message)