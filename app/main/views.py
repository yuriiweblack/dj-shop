from django.shortcuts import render
from django.http import HttpResponse


from goods.models import Categories

def index(request):
    
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - About',
        'content': 'About HOME',
        'some_text_about': 'About Lorem  ipsum dolor', 
    }
    return render(request, 'main/about.html', context)