from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'culinary_recipes/pages/home.html', context={
        'name': 'zerobala',
    })
