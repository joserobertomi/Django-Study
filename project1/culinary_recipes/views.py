from django.shortcuts import render, get_list_or_404
from utils.culinary_recipes.factorys import make_recipe
from culinary_recipes.models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'culinary_recipes/pages/home.html', context={'recipes': recipes})


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))

    return render(request, 'culinary_recipes/pages/categorys.html', context={
        'recipes': recipes,
        'category_title': f'{recipes[0].category.name}'
    })


def recipe(request, id):
    return render(request, 'culinary_recipes/pages/recipe_card.html', context={'recipe': make_recipe(), 'is_detail_page': True})
