from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'some_text': 'HOME Lorem ipsum dolor sit amet consectetur adipisicing elit.', 
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - About',
        'content': 'About HOME',
        'some_text_about': 'About Lorem  ipsum dolor', 
    }
    return render(request, 'main/about.html', context)