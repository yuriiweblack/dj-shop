from django.shortcuts import render
from goods.models import Products

# Create your views here.

def catalog(request):

    goods = Products.objects.all()

    context = {
        'title': 'Home - Головна',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    # context = {
    #     'title': 'Home - About',
    #     'content': 'About HOME',
    #     'some_text_about': 'About Lorem  ipsum dolor', 
    # }
    return render(request, 'goods/product.html')