from django.urls import path
from .views import sign_up, sign_in, log_out, home_route, start_route

urlpatterns = [
    path('', start_route),
    path('home', home_route, name='home'),
    path('register', sign_up, name='register'),
    path('login', sign_in, name='login'),
    path('logout', log_out, name='logout')
]