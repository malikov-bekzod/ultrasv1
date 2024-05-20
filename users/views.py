from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.views import View

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")

    def post(sefl, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            context = {"user": user}
            return redirect("home")
        return redirect("login")


class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html")

    def post(self, request):
        password = request.POST["password"]
        re_pass = request.POST["re_pass"]
        data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "username": request.POST["username"],
            "password": request.POST["password"],
        }
        register_form = UserRegisterForm(data=data)
        if register_form.is_valid() and password == re_pass:
            register_form.save()
            return redirect("login")
        return redirect("register")


class LogOutView(View):
    def get(self,request):
        logout(request)
        return redirect("home")