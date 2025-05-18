from django.core.paginator import Paginator
from django.shortcuts import Http404, render
from goods.models import Products

# Create your views here.

def catalog(request, category_slug):

    page = request.GET.get('page', 1)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug = category_slug)
        if not goods:
            raise Http404   

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)


    context = {
        'title': 'Home - Головна',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    
    product = Products.objects.get(slug = product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context = context)