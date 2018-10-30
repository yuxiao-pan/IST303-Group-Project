from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.core import serializers

from .service.authentication import Signup
from .service.news_service import CategoryService
from .service.news_service import NewsService
from .models import Category


#### Controllers
def health(request):
    return HttpResponse("Application news portal Started", content_type="text/plain")

def home(request):
    if request.user.is_authenticated:
        categories = CategoryService().getAll()
        news = NewsService().getAll()
        context = {
            "categories":categories,
            "news":getPreviewNews(news),
            "trend":getPreviewNews(news)
        }
        return render(request, 'dashboard.html', context)
    else:
        categories = CategoryService().getPublic()
        news = NewsService().getPublic()
        
        context = {
            "categories":categories,
            "news":getPreviewNews(news),
            "trend":getPreviewNews(news)
        }
        return render(request, 'home.html', context)

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


def newsdetail(request, news_id):
    news = NewsService().getById(news_id).values()
    if len(news) > 0:
        news= news[0]
    else:
        raise Http404("News does not exist")

    if (news['content_type_id'] == 1 and request.user.is_authenticated != 1):
        return HttpResponse("Signup to view news", content_type="text/plain")
    return JsonResponse(news, safe=False)

def newscategory(request):
    if request.user.is_authenticated:
        categories = CategoryService().getAll()
        news = NewsService().getAllByCategoryId(request.GET.get('cat'))
        context = {
            "categories": categories,
            "news" : getPreviewNews(news),
            "trend": getPreviewNews(news)
        }
        return render(request, 'dashboard.html', context)
    else:
        categories = CategoryService().getPublic()
        news = NewsService().getPublicByCategoryId(request.GET.get('cat'))
        context = {
            "categories": categories,
            "news" : getPreviewNews(news),
            "trend": getPreviewNews(news)
        }
        return render(request, 'home.html', context)

## helper methods
def getPreviewNews(news):
    for item in news:
        item.content = item.content[0:200]
    return news

def getTrendingNews():
    pass ## TODO