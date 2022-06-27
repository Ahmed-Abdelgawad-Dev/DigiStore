from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .cart import Cart
from product.models import Product


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, 'cart/menu_cart.html')


def cart(request):
    return render(request, 'cart/cart.html')


@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')


def menu_cart(request):
    return render(request, 'cart/menu_cart.html')


def update_cart(request, product_id, action):
    cart = Cart(request)
    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)['quantity']
    item = {
        "product": {
            "id": product.id,
            "name": product.name,
            "image": product.image,
            'get_thumbnail': product.get_thumbnail(),
            'price': product.price,

        },
        'quantity': quantity,
        "total_price": (quantity * product.price),
    }
    resp = render(request, 'cart/reusable/cart_item.html', {'item': item})
    resp['HX-Trigger'] = 'update-menu-cart'
    return resp


def cart_total(request):
    return render(request, 'cart/reusable/cart_total.html')
