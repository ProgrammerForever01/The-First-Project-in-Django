from django.db import models
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateTimeField(auto_now=True)
