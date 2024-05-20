from django.db import models
from blog.models import Blog
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return f"{self.text[:10]}"
