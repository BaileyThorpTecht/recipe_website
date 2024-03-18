from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'hello/home.html', context)

def about(request):
    return render(request, 'hello/home.html', {'title': 'about page'})