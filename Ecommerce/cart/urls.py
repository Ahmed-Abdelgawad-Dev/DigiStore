from django.urls import path
from cart.views import (
    add_to_cart, cart, checkout,
    menu_cart, update_cart, cart_total
)


urlpatterns = [

    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('menu_cart/', menu_cart, name='menu_cart'),  # htmx
    path('update_cart/<int:product_id>/<str:action>/',  # htmx
         update_cart, name='update_cart'),
    path('cart_total/', cart_total, name='cart_total'),  # htmx


]
