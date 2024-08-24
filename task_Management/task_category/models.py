from django.db import models
from task.models import Task
# Create your models here.
class TaskCategory(models.Model):
    name=models.CharField(max_length=100)
    tasks = models.ManyToManyField(Task, related_name="categories")
   
def __str__(self):
    return self.name
