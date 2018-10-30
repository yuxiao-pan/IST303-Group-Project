from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('health', views.health, name='health'),
    path('pages/signup',views.signup,name='signup-page'),
    path('pages/dashboard', views.dashboard, name='dashboard'),
    path('pages/news/<int:news_id>', views.newsdetail, name='news-detail')
]