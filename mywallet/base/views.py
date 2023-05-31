from django.shortcuts import render, redirect
from django.urls import *

# Create your views here.

def home(req):
    return render(req, "index.html")