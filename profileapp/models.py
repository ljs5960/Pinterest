from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # OneToOneField -> 1:1 Django function, on_delete=CASCADE -> Must deleted when User is deleted
  image = models.ImageField(upload_to='profile/', null=True)
  nickname = models.CharField(max_length=20, unique=True, null=True)
  message = models.CharField(max_length=100, null=True)