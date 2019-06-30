from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the category for this book')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Book title')
    author = models.CharField(max_length=400, help_text='Author', null=True, blank=True)
    description = models.TextField(help_text='Brief description', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    url =  models.URLField(max_length=500, help_text='Book url', unique=True, null=True)
    # category = ManyToManyField(category)
    # image = models.ImageField()

    class Meta:
        ordering = ['date_added']
    
    def __str__(self):
        return self.title

