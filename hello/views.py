import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

#data that gets passed through to template
recipes = [
    {
        "title": "Soup",
        "author": "Bailey",
        "content": "You put the sauce and meat in the bowl then cook it",
        "date_posted": "today"
    },
    {
        "title": "beans",
        "author": "Billy",
        "content": "You plant em and you grow em",
        "date_posted": "January 8th 2023"
    }
]


def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, 'hello/home.html', context)