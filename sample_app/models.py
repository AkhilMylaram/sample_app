from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task=models.TextField(max_length=200)


    def __str__(self):
        return f"{self.task}"

class media(models.Model):
    img=models.ImageField(upload_to='photos/')
