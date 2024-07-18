from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import Recipe
from .serializers import RecipeCreateSerializer, RecipeDetailSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer

    def get_serializer_class(self):
        """Return appropriate serializer class based on action"""
        if self.action in ['list', 'retrieve']:
            return RecipeDetailSerializer
        return RecipeCreateSerializer

    def create(self, request, *args, **kwargs):
        """Handle POST request to create a new recipe"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "message": "Recipe successfully created!",
            "recipe": [serializer.data]
        }, status=status.HTTP_200_OK, headers=headers)

    def list(self, request, *args, **kwargs):
        """Handle GET request to list all recipes"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "recipes": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """Handle GET request to retrieve a specific recipe by ID"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "message": "Recipe details by id",
            "recipe": [serializer.data]
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        """Handle PATCH request to update a specific recipe by ID"""
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Recipe successfully updated!",
            "recipe": [serializer.data]
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """Handle DELETE request to delete a specific recipe by ID"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "message": "Recipe successfully removed!"
            }, status=status.HTTP_200_OK)
        except Recipe.DoesNotExist:
            return Response({
                "message": "No recipe found"
            }, status=status.HTTP_404_NOT_FOUND)
