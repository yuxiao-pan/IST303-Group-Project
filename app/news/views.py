from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .service.authentication import Signup

def health(request):
    return HttpResponse("Application news portal Started", content_type="text/plain")

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.method == 'POST':
        Signup.create_user(request)
        return redirect('dashboard')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout(request):
    return render(request, 'dashboard.html')