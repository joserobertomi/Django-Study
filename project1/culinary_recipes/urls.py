from django.urls import path
from culinary_recipes.views import home


urlpatterns = [
    path('home', home),

]
