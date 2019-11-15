from rest_framework import serializers

from core.models import Tag, Ingredint

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

class IngredintSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Ingredint
        fields = ('id', 'name')
        read_only_fields = ('id',)