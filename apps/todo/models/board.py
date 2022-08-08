from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    """Board model"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    title = models.CharField(max_length=120)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
