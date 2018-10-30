from django.http import Http404

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

class CategoryService():
    def __init__(self):
        pass
    
    def getAll(self):
        try:
            categories = Category.objects.all()
        except categories.DoesNotExist:
            raise Http404("Category does not exist")
        return categories 