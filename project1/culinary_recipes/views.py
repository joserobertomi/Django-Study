from django.shortcuts import render
from utils.culinary_recipes.factorys import make_recipe
from culinary_recipes.models import Recipe
from django.http import Http404

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'culinary_recipes/pages/home.html', context={'recipes': recipes})


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404("Page Not Found 😢")

    return render(request, 'culinary_recipes/pages/categorys.html', context={
        'recipes': recipes,
        'category_title': f'{recipes.first().category.name}'
    })


def recipe(request, id):
    return render(request, 'culinary_recipes/pages/recipe_card.html', context={'recipe': make_recipe(), 'is_detail_page': True})
