from django.contrib.sites.shortcuts import get_current_site
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login, home, register, start_route, logout, profile, \
    forum, add_post, post_view, delete_post, create_comment, delete_comment, like_post, dislike_post, \
    follow_or_unfollow, edit_profile, activate_user, activate_account_complete, messages_page, create_message, \
    delete_message


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
    path('edit_profile', edit_profile, name='edit_profile'),
    path('messages', messages_page, name='messages'),
    path('create_message', create_message, name='create_message'),
    path('delete_message/<int:message_id>', delete_message, name='delete_message'),

    path('activate_user/<uidb64>/<token>/', activate_user, name='activate'),
    path('activate_account_complete', activate_account_complete, name='activate_account_complete'),


    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(
        template_name='reset_and_activate/password_reset/password_change_done.html'), name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='reset_and_activate/password_reset/password_change.html'), name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset_and_activate/password_reset/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset_and_activate/password_reset/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="reset_and_activate/password_reset/password_reset_form.html",
        html_email_template_name="reset_and_activate/password_reset/password_reset_email.html",
        email_template_name="reset_and_activate/password_reset/password_reset_email.html",
        subject_template_name="reset_and_activate/password_reset/password_reset_subject.txt"

    ), name='password_reset'),

    path('reset/done', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset_and_activate/password_reset/password_reset_complete.html'), name='password_reset_complete'),
]