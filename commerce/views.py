from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .forms import RegisterForm, LoginForm
from django.views import View
import requests

TOKEN_URL = "http://127.0.0.1:8000/api/token/"

class Regsiter(View):
    permission_classes = [AllowAny]

    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User.objects.create_user(
                username=username, 
                email=email,
                password=password
            )

            messages.success(request, "Registration successful! please login.")
            return redirect("login")

        return render(request, "register.html", {"form": form})    
    

class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            response = requests.post(TOKEN_URL, data={
                "username": username,
                "password": password
            })

            if response.status_code == 200:
                tokens = response.json()
                request.session['access'] = tokens['access']
                request.session['refresh'] = tokens['refresh']
                request.session['user'] = username

                messages.success(request, f"Welcome back {username}!")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password!")
    
        return render(request, "login.html", {"form": form})
    

class Logout(View):

    def get(self, request):
        request.session.flush()
        messages.success(request, "You have been logged out!")
        return redirect("login")
    

class Dashboard(View):
    def get(self, request):
        access = request.session.get("access")

        if not access:
            messages.error(request, "Please login first")
            return redirect("login")
        
        return render(request, "home.html", {
            "user": request.session.get("user")
        })






