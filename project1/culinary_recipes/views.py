from django.shortcuts import render
from utils.culinary_recipes.factorys import make_recipe
from culinary_recipes.models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'culinary_recipes/pages/home.html', context={'recipes': recipes})


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'culinary_recipes/pages/home.html', context={'recipes': recipes})


def recipe(request, id):
    return render(request, 'culinary_recipes/pages/recipe_card.html', context={'recipe': make_recipe(), 'is_detail_page': True})
