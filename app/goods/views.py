from django.shortcuts import Http404, render
from goods.models import Products

# Create your views here.

def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug = category_slug)
        if not goods:
            raise Http404   

    context = {
        'title': 'Home - Головна',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    
    product = Products.objects.get(slug = product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context = context)