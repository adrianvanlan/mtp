from django.shortcuts import render, redirect, render_to_response
from django.http import request

# Create your views here.

def index(request):
	return render_to_response("index.html", {})
