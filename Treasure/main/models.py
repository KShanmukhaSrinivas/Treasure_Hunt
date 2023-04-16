from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content= models.TextField()
    def __str__(self):
        return self.title


class Progress(models.Model):
    level1 = models.BooleanField()
    
    level2 = models.BooleanField()
    level3 = models.BooleanField()
    # content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    