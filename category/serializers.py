from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent.name')

    class Meta:
        model = Category
        fields = '__all__'


    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name должно содержать не менее 3 символов.")
        return value

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        parents = instance.parents.all()
        if parents:
            repr['children'] = CategorySerializer(
                parents, many=True
            ).data
        return repr
