from django.shortcuts import render
from .models import Customer, Product, Order, OrderItem, ShippingAdress
from django.http import JsonResponse
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from .utils import cookieCart, cartData, guestOrder

def main(request):
    context = {}
    return render(request, 'store/main.html', context)


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items'] 
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


@csrf_exempt
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action    = data['action']
    print('productId => ', productId)
    print('action    => ', action)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('data from views returned by JsonResponse', safe=False)


@csrf_exempt
def processOrder(request):
    transaction_id = datetime.now().timestamp()
    data = json.loads(request.body)
    print('data =>  ',data)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        

    else:
        customer, order = guestOrder(request, data)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
            order.complete = True
    order.save()
    if order.shipping == True:
        ShippingAdress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            # zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('payment complete...', safe=False)
