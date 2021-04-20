from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from datetime import datetime
import requests
import json
# Create your views here.

def index(request):
    return render(request, "MyDiary/index.html")


def myAccount(request):
    context = {
        "Name": request.user.first_name + " " + request.user.last_name,
        "Email": request.user.email,
        "Username": request.user.username
    }

    return render(request, "MyDiary/myAccount.html", context)

def sign_up(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        user = User.objects.create_user(username, email, password)
        if user is not None:
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            return render(request, "MyDiary/index.html")
        else:
            return render(request, "MyDiary/sign_up.html", {"message": "Invalid input"})
    else:
        return render(request, "MyDiary/sign_up.html", {"message": "Wrong Method"})

def logIn(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, "MyDiary/log_in.html")
    else:
        return render(request, "MyDiary/log_in.html")

def logOut(request):
    logout(request)
    return render(request, "MyDiary/log_in.html", {"message": "Logged out."})
