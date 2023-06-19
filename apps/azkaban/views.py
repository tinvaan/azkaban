
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# TODO: Enable login_required after implementing login view
# @login_required
def home(request):
    return render(request, "azkaban/home.html")


def login(request):
    user = auth.authenticate(
        request, username=request.POST.get('username'), password=request.POST.get('password')
    )
    if user:
        auth.login(request, user)
        return render(request, "azkaban/home.html")
    return render(request, "azkaban/login.html", {'error': 'Login failed'})


@login_required
def logout(request):
    auth.logout()
    return redirect("/")
