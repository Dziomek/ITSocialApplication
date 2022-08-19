from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import auth
from .models import CustomUser, Profile
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .functions import make_birthday_date


# Create your views here.


def start_route(request):
    return redirect('home')


@login_required(login_url='login')
def home(request):
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user)

    return render(request, 'pages/home_base.html', {'current_user': current_user,
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

    return render(request, 'pages/profile_page.html', {'current_user': current_user,
                                                       'user_profile': user_profile,
                                                       'searched_user': searched_user,
                                                       'searched_profile': searched_profile})
