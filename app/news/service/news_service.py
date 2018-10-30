from django.http import Http404
from django.shortcuts import get_object_or_404

from ..models import Category
from ..models import News


class NewsService():
    def __init__(self):
        pass

    def getAll(self):
        try:
            news = News.objects.all()
        except news.DoesNotExist:
            raise Http404("News does not exist")
        return news
    
    def getById(self, id):
        try:
            news = News.objects.filter(id=id)
        except news.DoesNotExist:
            raise Http404("News ID does not exist")
        return news
    
    def getPublic(self):
        try:
            news = News.objects.filter(content_type_id=2)
        except news.DoesNotExist:
            raise Http404("Error getting news")
        return news

class CategoryService():
    def __init__(self):
        pass
    
    def getAll(self):
        try:
            categories = Category.objects.all()
        except categories.DoesNotExist:
            raise Http404("Category does not exist")
        return categories 

    def getPublic(self):
        try:
            categories = Category.objects.filter(content_type_id=2)
        except categories.DoesNotExist:
            raise Http404("Error getting news")
        return categories