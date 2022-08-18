from django.urls import path
from .views import login, home_route, register

urlpatterns = [
    path('', login, name='login'),
    path('register', register, name='register'),
    path('home', home_route, name='home')
]