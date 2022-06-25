from django.urls import path
from core.views import main, shop
from product.views import product

urlpatterns = [
    path('', main, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]
