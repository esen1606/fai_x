from rest_framewk import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'

