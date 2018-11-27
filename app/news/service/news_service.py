from django.http import Http404
from django.shortcuts import get_object_or_404

from ..models import Category
from ..models import News
from ..models import Comment


class NewsService():
    def __init__(self):
        pass

    def getAll(self):
        news = None
        try:
            news = News.objects.all()
        except news.DoesNotExist:
            raise Http404("News does not exist")
        return news
    
    def getById(self, id):
        news = None
        try:
            news = News.objects.get(id=id)
        except:
            raise Http404("News ID does not exist")
        return news
    
    def getPublic(self):
        try:
            news = News.objects.filter(content_type_id=2)
        except news.DoesNotExist:
            raise Http404("Error getting news")
        return news

    def getAllByCategoryId(self, id):
        try:
            news = News.objects.filter(category_id=id)
        except news.DoesNotExist:
            raise Http404("Error getting news")
        return news

    def getPublicByCategoryId(self, id):
        try:
            news = News.objects.filter(category_id=id, content_type_id=2)
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

class CommentService():
    def __init__(self):
        pass
    
    def getByNewsId(self, news_id):
        try:
            comments = Comment.objects.filter(news_id=news_id)
        except comments.DoesNotExist:
            raise Http404("Comment does not exist")
        return comments 

    def saveNewComment(self, form_data):
        try:
            news = NewsService().getById(form_data["news_id"])
            comments = Comment(text=form_data["text"], news = news, user = form_data["user"])        
            comments.save()
        except:
            raise Http404("Could not save comment")

