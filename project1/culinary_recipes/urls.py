from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('recipe/<id>/', views.recipe)
]
