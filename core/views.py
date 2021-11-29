import os
import h5py
import numpy as np
from PIL import Image
import tensorflow as tf
from secrets import token_hex
from django.conf import settings
from django.shortcuts import render
from .models import Food, Ingredient, Recipe
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

DATASET = settings.DATASET
MODEL = settings.MODEL

def predict(images):
    """
    A function to get labels for input images using a trained model
    """
    file = h5py.File(DATASET, "r")
    model = tf.keras.models.load_model(MODEL)
    predictions = model.predict(images)
    argmaxs = np.argmax(predictions, axis = 1)
    labels = []
    
    for x in argmaxs:
        labels.append(file["category_names"][x].decode('ascii'))

    return labels

def get_recipe_data(labels, urls):
    recipes = []

    for label, url in zip(labels, urls):
        new_label = " ".join(label.lower().split("_"))
        food = Food.objects.filter(name = new_label)

        if not food.exists():
            continue
        
        food = food.first()
        recipe = food.recipes.all().order_by("?").first()
        ingredients = recipe.ingredients.all()
        recipes.append((recipe, ingredients, url))

    return recipes

def load_images(paths):
    finals = []

    for path in paths:
        image = Image.open(path)
        image = np.asarray(image)
        finals.append(image)
        
    return np.array(finals)

def index(request):
    """
    View for home or index page
    """
    images = []
    recipes = []
    paths = []
    urls = []

    if request.method == "POST":
        images = request.FILES.getlist("images")

        for image in images:
            path = default_storage.save(f"{token_hex(16)}.png", ContentFile(image.read()))
            urls.append(settings.MEDIA_URL + path)
            paths.append(os.path.join(settings.MEDIA_ROOT, path))

        images = load_images(paths)
        images = np.array(images)
        labels = predict(images)
        recipes = get_recipe_data(labels, urls)

    return render(request, "core/index.html", {
        "images": images,
        "recipes": recipes
    })