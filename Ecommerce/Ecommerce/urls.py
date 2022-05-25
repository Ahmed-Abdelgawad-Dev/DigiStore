"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from cart.views import add_to_cart, cart
from core.views import main, shop, signup, login2
from product.views import product

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),

    path('', main, name='shop'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('signup/', signup, name='signup'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
