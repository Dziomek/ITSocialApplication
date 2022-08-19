from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import auth
from .models import CustomUser
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .functions import make_birthday_date

# Create your views here.


def start_route(request):
    return redirect('login')


def home_route(request):
    return render(request, 'pages/home.html')


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
                    messages.info(request, "User with this email already exists. Please try again")
                elif CustomUser.objects.filter(username=username).exists():
                    messages.info(request, "User with this name already exists. Please try again")
                else:
                    CustomUser.objects.create_user(email=email, username=username, firstname=first_name,
                                                   lastname=last_name, birthday=birthday, gender=gender,
                                                   password=password)
                    messages.info(request, "User created successfully")
        else:
            messages.info(request, "Missing data. Please try again")
    return redirect('login')


def logout(request):
    pass