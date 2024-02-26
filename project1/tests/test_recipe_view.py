from django.test import TestCase
from django.urls import reverse, resolve
from culinary_recipes.views import home, category, recipe


class RecipeViewTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('culinary_recipes:home'))
        self.assertIs(view.func, home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('culinary_recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('culinary_recipes:home'))
        self.assertTemplateUsed(response, 'culinary_recipes/pages/home.html')

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('culinary_recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, category)

    def test_recipe_recipe_views_function_is_correct(self):
        view = resolve(reverse('culinary_recipes:card', kwargs={'id': 1}))
        self.assertIs(view.func, recipe)