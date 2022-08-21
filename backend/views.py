from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import auth
from .models import CustomUser, Profile, Post, Comment
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .functions import make_birthday_date, get_number_of_comments


# Create your views here.


def start_route(request):
    return redirect('home')


@login_required(login_url='login')
def home(request):
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user)

    return render(request, 'pages/home_page.html', {'current_user': current_user,
                                                    'user_profile': user_profile})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Credentials invalid. Please try again")
            return redirect('login')

    else:
        return render(request, 'pages/start_page.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        gender = request.POST['other']
        year = request.POST['Year']
        month = request.POST['Month']
        day = request.POST['Day']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        birthday = make_birthday_date(year, month, day)

        if first_name and last_name and username and email and password and confirm_password and gender and birthday:
            if password == confirm_password:
                if CustomUser.objects.filter(email=email).exists():
                    messages.info(request, "User with this email already exists")
                elif CustomUser.objects.filter(username=username).exists():
                    messages.info(request, "User with this name already exists")
                else:
                    user = CustomUser.objects.create_user(email=email, username=username, firstname=first_name,
                                                          lastname=last_name, birthday=birthday, gender=gender,
                                                          password=password)
                    profile = Profile(user=user)
                    profile.save()

                    messages.info(request, "User created successfully")
            else:
                messages.info(request, "Passwords don't match. Please try again")
        else:
            messages.info(request, "Missing data. Please try again")
    return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request, username):
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user)
    searched_user = CustomUser.objects.get(username=username)
    searched_profile = Profile.objects.get(user=searched_user)
    posts = Post.objects.filter(user=searched_user)
    print(posts)

    return render(request, 'pages/profile_page.html', {'current_user': current_user,
                                                       'user_profile': user_profile,
                                                       'searched_user': searched_user,
                                                       'searched_profile': searched_profile,
                                                       'posts': posts})


@login_required(login_url='login')
def forum(request):
    posts = Post.objects.all().order_by('-id')
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user)
    comments = Comment.objects.all()

    get_number_of_comments()

    return render(request, 'pages/forum_page.html', {'current_user': current_user,
                                                     'user_profile': user_profile,
                                                     'posts': posts,
                                                     'comments': comments})


@login_required(login_url='login')
def add_post(request):
    current_user = request.user

    if request.method == 'POST':
        topic = request.POST['topic']
        content = request.POST['content']
        picture = request.POST['picture']

        if content:
            post = Post(user=current_user, topic=topic, content=content, picture=picture)
            post.save()
    return redirect('forum')


@login_required(login_url='login')
def post_view(request, post_id):
    current_user = request.user
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.all()

    return render(request, 'pages/post_page.html', {'post': post,
                                                    'current_user': current_user,
                                                    'comments': comments})


@login_required(login_url='login')
def delete_post(request, post_id):
    current_user = request.user
    post = Post.objects.get(id=post_id, user=current_user)
    if post:
        post.delete()

    return redirect('forum')


@login_required(login_url='login')
def create_comment(request, post_id):

    if request.method == 'POST':
        current_user = request.user
        post = Post.objects.get(id=post_id)
        post.number_of_comments += 1
        post.save()
        content = request.POST['content']
        comment = Comment(post=post, user=current_user, content=content)
        comment.save()

    return redirect('post_view', post_id=post_id)


@login_required(login_url='login')
def delete_comment(request, comment_id, post_id):
    current_user = request.user
    post = Post.objects.get(id=post_id)
    post.number_of_comments -= 1
    post.save()
    comment = Comment.objects.get(id=comment_id, user=current_user)
    if comment:
        comment.delete()



    return redirect('post_view', post_id=post_id)
