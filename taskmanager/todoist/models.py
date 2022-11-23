from django.db import models

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length = 100)

    content = models.CharField(max_length = 1000)

    date_posted = models.DateTimeField(auto_now_add = True)