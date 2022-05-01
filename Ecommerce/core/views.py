from django.shortcuts import render
from product.models import Product


def main(request):
    products = Product.objects.all()[0:6]
    context = {'products': products}
    return render(request, 'core/frontpage.html', context)


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'core/shop.html', context)
