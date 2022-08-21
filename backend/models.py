import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.contrib.auth.models import User


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, birthday, gender, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, firstname=firstname, lastname=lastname, birthday=birthday,
                          gender=gender, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, firstname, lastname, birthday, gender, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, username, firstname, lastname, birthday, gender, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    birthday = models.TextField()
    gender = models.TextField()
    is_active = models.BooleanField(default=True)  # pozniej doda sie jakas aktywacje maila i bedzie aktywny
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    profile_img = models.ImageField(upload_to='profile_images', default='blank_profile_picture.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'birthday', 'gender']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    about = models.TextField(null=True)
    location = models.CharField(max_length=150, null=True)


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    topic = models.TextField()
    content = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()