from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Book title ")
    # author = 
    description = models.TextField(help_text="Brief description ", null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # image = models.ImageField()

    class Meta:
        ordering = ['date_added']

    
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('book-detail', args=[str(self.id)]))