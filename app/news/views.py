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
    signup = Signup()
    if request.method == 'POST':        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            signup.create_user(form)
            signup.login_user(form, request)
            return redirect('dashboard')
    else:
        form = signup.create_form()
    return render(request, 'signup.html', {'form': form})

def logout(request):
    return render(request, 'dashboard.html')