from django.contrib import admin
from .models import Recipe, Ingredient, Food

class RecipeAdmin(admin.ModelAdmin):
    list_display = ["get_food_name", "get_ingredients"]

    def get_food_name(self, object):
        return object.food.name

    get_food_name.short_description = "Food Name"

    def get_ingredients(self, object):
        return object.get_ingredients()

    get_ingredients.short_description = "Ingredients"

class FoodAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "slug"]

class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

admin.site.register(Food, FoodAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)