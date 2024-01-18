from django.db import models
from category.models import Category
from account.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True)
    preview = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


class PostImages(models.Model):
    title = models.CharField(max_length=100, blank=True)
    images = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)

    def generate_name(self):
        from random import randint
        return 'image' + str(randint(100_000, 1_000_000))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(PostImages, self).save(*args, **kwargs)
    
class Video(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video_url = models.URLField()
