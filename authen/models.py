
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length= 250)

    def __str__(self):
        return self.title


class MyUser(AbstractUser):
    age = models.IntegerField(default=0)
    gender_choice = ((0,'Female'),(1,'Male'))
    gender = models.IntegerField(choices=gender_choice, default=0)
    address = models.CharField(default='', max_length=255)