from django.db import models
from django.contrib.auth.models import User

from .board import Board


class Column(models.Model):
    """Column model"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
