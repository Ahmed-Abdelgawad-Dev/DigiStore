from django.shortcuts import render
# Create your views here.


def main(request):
    context = {}
    return render(request, 'store/main.html', context)


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)
