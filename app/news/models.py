from django.db import models

# Create your models here.

class ContentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=True, max_length = 50)
    content = models.CharField(max_length=5000)
    publish_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=True, max_length = 50)
    text = models.CharField(max_length=1000)
    news_id = models.ForeignKey(News, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    alt_text = models.CharField(null=True, max_length = 50)
    news_id = models.ForeignKey(News, null=True, on_delete=models.SET_NULL)
    url = models.CharField(null=True, max_length = 200)

    def __str__(self):
        return self.alt_text




