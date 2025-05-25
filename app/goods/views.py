from django.core.paginator import Paginator
from django.shortcuts import Http404, render
from goods.models import Products
from goods.utils import q_search

# Create your views here.

def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    # print(on_sale,order_by)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug = category_slug)
        if not goods:
            raise Http404   

    if on_sale:
        print(goods)
        goods = goods.filter(discont=0)
        print(goods)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))


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