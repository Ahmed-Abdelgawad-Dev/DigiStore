from django.urls import path
from .views import make_order


urlpatterns = [
    path('make_order/', make_order, name='make_order'),
]
