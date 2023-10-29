
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'navbar': 'home'})


def home(request):
    return render(request, 'home.html', {'navbar': 'home'})