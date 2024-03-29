from django.shortcuts import render, redirect
from product.models import Product, Category
from django.db.models import Q
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def main(request):
    products = Product.objects.all()
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


@login_required
def user_account(request):
    return render(request, 'core/user_account.html')


@login_required
def edit_user_account(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        print('USER====================>>>>>>>>>>>>>>', user.first_name)
        print('USER====================>>>>>>>>>>>>>>', user.last_name)
        print('USER====================>>>>>>>>>>>>>>', user.username)
        print('USER====================>>>>>>>>>>>>>>', user.email)
        user.save()

        return redirect('user_account')
    return render(request, 'core/edit_user_account.html')
