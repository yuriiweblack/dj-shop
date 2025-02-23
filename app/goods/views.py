from django.shortcuts import render

# Create your views here.

def catalog(request):
    # context = {
    #     'title': 'Home - Главная',
    #     'content': 'Магазин мебели HOME',
    #     'some_text': 'HOME Lorem ipsum dolor sit amet consectetur adipisicing elit.', 
    # }
    return render(request, 'goods/catalog.html')


def product(request):
    # context = {
    #     'title': 'Home - About',
    #     'content': 'About HOME',
    #     'some_text_about': 'About Lorem  ipsum dolor', 
    # }
    return render(request, 'goods/product.html')