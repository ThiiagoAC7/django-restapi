from django.db import models

from django.utils import timezone 


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

