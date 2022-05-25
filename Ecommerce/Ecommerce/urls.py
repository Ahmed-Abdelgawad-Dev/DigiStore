from re import template
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from cart.views import add_to_cart, cart, checkout
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
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
