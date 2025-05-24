from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):    
        return self.title



    