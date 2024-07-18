from django.contrib import admin

from recipes.models import Recipe

admin.site.site_header = "Recipe ADMIN"


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'making_time', 'serves', 'ingredients', 'cost', 'created_at', 'updated_at']
