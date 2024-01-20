from django.db import models
from category.models import Category
from account.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True)
    images = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    video_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


    



