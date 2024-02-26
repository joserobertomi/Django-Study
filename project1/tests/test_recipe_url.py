from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):

    def test_culinary_recipes_home_url_is_correct(self):
        home_url = reverse('culinary_recipes:home')
        self.assertEqual(home_url, '/')

    def test_culinary_recipes_category_home_url_is_correct(self):
        category_url = reverse('culinary_recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipe/category/1/')

    def test_Culinary_recipes_detail_card_url_is_correct(self):
        datail_card_url = reverse('culinary_recipes:card', kwargs={'id': 1})
        self.assertEqual(datail_card_url, '/recipe/1/')