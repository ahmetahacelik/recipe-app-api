from rest_framework import serializers

from core.models import Tag, Ingredint, Recipe

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


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    ingredints = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredint.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredints', 'tags', 'time_minutes', 'price',
            'link',
        )
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    ingredints = IngredintSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True,read_only=True)
    