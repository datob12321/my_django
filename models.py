from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Image(models.Model):
    image = models.URLField(null=False)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)





