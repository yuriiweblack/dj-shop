from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'content': 'Main shop page - HOME',
        'list': ['first', 1],
        'dict': {'second': 2},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('Hello ABOUT page')