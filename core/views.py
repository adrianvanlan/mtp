from django.shortcuts import render, redirect, render_to_response
from django.http import request
from django.contrib.auth import authenticate, login

def index(request):
    return render_to_response("index.html", {})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        render_to_response("index.html", {})
    else:
        render_to_response("index.html", {})
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)


def mapa(request):
    return render_to_response("mapa.html", {})
