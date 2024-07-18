from django.urls import path, include
from rest_framework import routers

from recipes.views import RecipeViewSet

recipes_router = routers.DefaultRouter()

""" Recipe View Routers """
recipes_router.register('recipes', RecipeViewSet)

urlpatterns = [
    # path('api/', include('recipes.urls')),
]
