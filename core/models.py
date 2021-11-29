from enum import unique
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length = 250, unique = True)
    slug = models.SlugField(max_length = 250, unique = True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length = 250, unique = True)
    slug = models.SlugField(max_length = 250, unique = True)
    quantity = models.IntegerField(default = 0)
    calories = models.FloatField(default = 0.0)

    def __str__(self):
        return self.name

    def get_calories_per_quantity(self):
        if self.quantity == 0:
            return 0.0

        return self.calories / self.quantity

class Recipe(models.Model):
    food = models.ForeignKey(Food, on_delete = models.CASCADE, related_name = "recipes")
    ingredients = models.ManyToManyField(Ingredient)

    def get_ingredients(self):
        return ", ".join([x.name for x in self.ingredients.all()])

    def __str__(self):
        return f"{self.food.name} > {self.get_ingredients()}"