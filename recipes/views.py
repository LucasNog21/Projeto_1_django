from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes= Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
        })

def category(request, category_id):
    recipes= Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
        })


def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

