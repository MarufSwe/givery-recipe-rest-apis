from rest_framework import serializers
from .models import Recipe


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'making_time', 'serves', 'ingredients', 'cost', 'created_at', 'updated_at']


class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'making_time', 'serves', 'ingredients', 'cost']
