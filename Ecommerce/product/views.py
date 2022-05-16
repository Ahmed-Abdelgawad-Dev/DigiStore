from django.shortcuts import get_object_or_404, render

from .models import Product


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'product/product.html', context)
