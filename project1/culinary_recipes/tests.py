from django.test import TestCase
from django.urls import reverse


class TestingSetUp(TestCase):

    def test_is_set_up_ok(self):
        assert 1 == 1, "OK"


class RecipeURLsTest(TestCase):

    def test_culinary_recipes_home_url_is_correct(self):
        home_url = reverse('culinary_recipes:home')
        self.assertEqual(home_url, '/')
