from django.db import models


# Model for storing recipe details
class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    making_time = models.CharField(max_length=100, blank=False, null=False)
    serves = models.CharField(max_length=100, blank=False, null=False)
    ingredients = models.TextField(blank=False, null=False)
    cost = models.IntegerField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
