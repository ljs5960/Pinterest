from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
  writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # on_delete=models.SET_NULL >> 외래키 삭제시 기존 게시물 user이름이 unknown으로 유지되게 설정
  title = models.CharField(max_length=200, null=True)
  image = models.ImageField(upload_to='article/', null=False)
  content = models.TextField(null=True)
  created_at = models.DateField(auto_created=True, null=True)