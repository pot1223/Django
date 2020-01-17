from django.db import models

class post(models.Model):
    author_name=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post=models.ForeignKey(post, on_delete=models.CASCADE)
    message=models.TextField()
