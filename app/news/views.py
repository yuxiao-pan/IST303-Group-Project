from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .service.authentication import Signup
from .service.news_service import CategoryService
from .service.news_service import NewsService
from .models import Category

def health(request):
    return HttpResponse("Application news portal Started", content_type="text/plain")

def home(request):
    categories = CategoryService().getAll()
    news = NewsService().getAll()
    
    context = {
        "categories":categories,
        "news":getPreviewNews(news)
    }
    return render(request, 'home.html', context)

def dashboard(request):
    categories = CategoryService().getAll()
    news = NewsService().getAll()
    context = {
        "categories":categories,
        "news":getPreviewNews(news)
    }
    return render(request, 'dashboard.html', context)

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

    categories = CategoryService().getAll()
    context = {
        "categories":categories,
        "form":form
    }
    return render(request, 'signup.html', context)

def logout(request):
    return render(request, 'dashboard.html')

def getPreviewNews(news):
    for item in news:
        item.content = item.content[0:200]
    return news
