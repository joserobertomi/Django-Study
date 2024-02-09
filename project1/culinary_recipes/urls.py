from django.urls import path
from . import views

app_name = 'culinary_recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/category/<int:category_id>/', views.category, name="category"),
    path('recipe/<id>/', views.recipe, name="card")
]
