from django.urls import path
from .views import login, home, register, start_route, logout, profile, \
    forum, add_post, post_view, delete_post, create_comment, delete_comment, like_post, dislike_post, follow_or_unfollow

urlpatterns = [
    path('', start_route),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('home', home, name='home'),
    path('logout', logout, name='logout'),
    path('profile/<str:username>', profile, name='profile'),
    path('forum', forum, name='forum'),
    path('add_post', add_post, name='add_post'),
    path('post/<int:post_id>', post_view, name='post_view'),
    path('delete_post/<int:post_id>', delete_post, name='delete_post'),
    path('comment/<int:post_id>', create_comment, name='create_comment'),
    path('delete_comment/<int:comment_id>/post=<int:post_id>', delete_comment, name='delete_comment'),
    path('like_post/<int:post_id>', like_post, name='like_post'),
    path('dislike_post/<int:post_id>', dislike_post, name='dislike_post'),
    path('follow/<str:username>', follow_or_unfollow, name='follow_or_unfollow'),
]