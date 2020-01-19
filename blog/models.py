from django.db import models
from first.utils import uuid_upload_to

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo=models.ImageField(blank=True,upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
