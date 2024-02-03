from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'culinary_recipes/home.html')


def about(request):
    return HttpResponse('About Page')


def contact(request):
    return HttpResponse('Contact Page')
