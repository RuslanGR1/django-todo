from django.db import models
from django.contrib.auth.models import User

from .board import Board
from .column import Column


class Task(models.Model):
    """Task model"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    orderNumber = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title
