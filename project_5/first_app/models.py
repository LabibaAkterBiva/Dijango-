from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField()
    fathers_name=models.TextField(default='Rahim')

    def __str__(self):
        return f"Roll :{self.name}-{self.roll}"