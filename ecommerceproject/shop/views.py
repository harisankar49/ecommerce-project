from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def allproductcat(request, c_slug=None):
    category_page = None
    products_list = None

    if c_slug is not None:
        category_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=category_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)



    return render(request, 'category.html', {'category': category_page, 'products': products})

def prodetails(request, c_slug, p_slug):
    product = get_object_or_404(Product, category__slug=c_slug, slug=p_slug)
    return render(request, 'product.html', {'product': product})
