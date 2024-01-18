from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from post.models import Post
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def add_like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    if Like.objects.filter(post=post, user=user).exists():
        return Response({"detail": "Вы уже поставили лайк."}, status=status.HTTP_400_BAD_REQUEST)
    like = Like(post=post, user=user)
    like.save()
    serializer = LikeSerializer(like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def remove_like(request, post_id):
    user = request.user 
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(post=post, user=user).first()
    if not like:
        return Response({"detail": "Вам не понравился этот пост."}, status=status.HTTP_400_BAD_REQUEST)
    like.delete()
    return Response({"detail": "Лайк удалили успешно."}, status=status.HTTP_204_NO_CONTENT)
