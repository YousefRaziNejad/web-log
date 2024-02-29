from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'نام کاربری نا معتبر هست')
            return redirect("login")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'رمز عبور نا معتبر هست')
            return redirect("login")
        else:
            login(request, user)
            return redirect("post-list")

    return render(request, "account/login.html")

def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect("register")

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username)

        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully!")
        return redirect("login")

    return render(request, "account/register.html")

def logout_view(request):
    logout(request)
    return redirect("post-list")