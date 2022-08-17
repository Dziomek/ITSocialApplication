from django.urls import path
from .views import sign_up, sign_in, logout, home_route

urlpatterns = [
    path('home', home_route, name='home'),
    path('register', sign_up, name='register'),
    path('login', sign_in, name='login'),
    path('logout', logout, name='logout')
]