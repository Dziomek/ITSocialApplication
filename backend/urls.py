from django.urls import path
from .views import login, home, register, start_route, logout, profile, forum, add_post

urlpatterns = [
    path('', start_route),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('home', home, name='home'),
    path('logout', logout, name='logout'),
    path('profile/<str:username>', profile, name='profile'),
    path('forum', forum, name='forum'),
    path('add_post', add_post, name='add_post')
]