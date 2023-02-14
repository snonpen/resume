from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    page = request.GET.get('page', 1)
    filter_by = request.GET.get('filter_by', 'all')
    if filter_by == 'available':
        products = products.filter(inventory__gt=0)
    elif filter_by == 'out_of_stock':
        products = products.filter(inventory=0)

    paginator = Paginator(products, 10)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/product_list.html', {'products': products})
