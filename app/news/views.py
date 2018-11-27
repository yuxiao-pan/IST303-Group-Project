from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.core import serializers
from django import forms

from .service.authentication import Signup
from .service.news_service import CategoryService
from .service.news_service import NewsService
from .service.news_service import CommentService
from .models import Category

user_not_supported =  {"error":"User not supported"}
method_not_supported = {"error":"method not supported"}

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
            return redirect('home')
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
    news = NewsService().getById(news_id)
    if news == None:
        raise Http404("News does not exist")
    news = news.__dict__
    comments = CommentService().getByNewsId(news_id)
    form = MessageForm(initial={'news_id':news_id})
    
    if (news['content_type_id'] == 1 and request.user.is_authenticated != 1):
        return HttpResponse("Signup to view news", content_type="text/plain")
    context = {
        "news":news,
        "categories": getCategory(request),
        "comments": comments,
        "form":form
    }
    #return JsonResponse(list(comments), safe=False)
    return render(request, 'content.html', context)

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

def newscomment(request):
    if(request.method=="POST"):
        if request.user.is_authenticated:
            form = MessageForm(request.POST)
            if form.is_valid():
                #print("break point 1")
                form_data = dict(form.cleaned_data)
                form_data["user"] = request.user  
                CommentService().saveNewComment(form_data)
                return redirect('news-detail', news_id = form_data["news_id"])
        else:
            return JsonResponse(user_not_supported, safe=False)
    else:
        return JsonResponse(method_not_supported, safe=False)

## helper methods
def getPreviewNews(news):
    for item in news:
        item.content = item.content[0:200]
    return news

def getTrendingNews():
    pass ## TODO

def getCategory(request):
    if request.user.is_authenticated:
        return CategoryService().getAll()
    else:
        return CategoryService().getPublic()

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea ,  label='Comment', max_length=100)
    news_id = forms.CharField()
    text.widget.attrs.update({'class':'form-control', 'rows':'5'})
    news_id.widget = forms.HiddenInput()

    

