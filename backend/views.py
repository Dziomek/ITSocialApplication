from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def start_route(request):
    return redirect('home')


@login_required(login_url='login')
def home_route(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if username and email and password and confirm_password:
            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "User with this email already exists. Please try again")
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, "User with this name already exists. Please try again")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    #Log user in and redirect to setting page

                    #create a profile object for the new user
                    user_model = User.objects.get(username=username)
                    #new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                    #new_profile.save()
                    return redirect('login')
            else:
                messages.info(request, "Passwords don't match. Please try again")
                return redirect('register')
        else:
            messages.info(request, "Missing fields. Please try again")
            return redirect('register')

    else:
        return render(request, 'registration.html')


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Credentials invalid. Please try again")
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url ='sign_in')
def log_out(request):
    auth.logout(request)
    return redirect('login')