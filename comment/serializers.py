from rest_framework import serializers
from post.models import Post
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.id')

    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['post_title'] = instance.post.title
        if instance.post.preview:
            preview = instance.post.preview
            representation['post_preview'] = preview.url
        else:
            representation['post_preview'] = None
        return representation


class CommentActionSerializer(serializers.ModelSerializer):
    username_ = serializers.ReadOnlyField(source='username.id')
    post = serializers.CharField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        post = self.context.get('post')
        post = Post.objects.get(pk=post)
        validated_data['post'] = post
        username = self.context.get('username')
        validated_data['username'] = username
        return super().create(validated_data)
