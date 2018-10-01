from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=140)
    task_date = models.DateTimeField()
