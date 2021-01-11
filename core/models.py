from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    answer = models.TextField(blank=True, max_length=2000)

    def __str__(self):
        return self.title 