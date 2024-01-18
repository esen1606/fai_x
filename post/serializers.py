from rest_framework import serializers
from .models import Post, PostImages, Video



class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields =  '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        post = Post.objects.create(**validated_data)
        images_data = request.FILES.getlist('images')
        for image in images_data:
            PostImages.objects.create(images=image, post=post)
        return post

class PostDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_url']

    