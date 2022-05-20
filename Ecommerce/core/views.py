from django.shortcuts import render, redirect
from product.models import Product, Category
from django.db.models import Q
from .forms import SignUpForm
from django.contrib.auth import login


def main(request):
    products = Product.objects.all()[0:6]
    context = {'products': products}
    return render(request, 'core/frontpage.html', context)


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category')

    if active_category:
        products = Product.objects.filter(category__slug=active_category)

    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(Q(name__icontains=query)
                                          | Q(description__icontains=query))

    context = {'products': products, 'categories': categories,
               'active_category': active_category}
    return render(request, 'core/shop.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(form)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})


def login2(request):
    return render(request, 'core/login.html')
