from django.db import models
from post.models import Post
from django.conf import settings

class Comment(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}  <--(UwU)-->  {self.post}'
