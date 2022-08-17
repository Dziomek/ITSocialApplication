from django.urls import path
from .views import signup, signin, logout, home_route

urlpatterns = [
    path('', home_route, name='index'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('logout', logout, name='logout')
]