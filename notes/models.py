from django.db import models
from datetime import datetime

# Create your models here.
class Note(models.Model):
    title = models.CharField(unique=True, max_length=200)
    body = models.TextField()
    time_updated = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
