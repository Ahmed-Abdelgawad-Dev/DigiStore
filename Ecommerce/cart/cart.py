from itertools import product
from django.conf import settings
from product.models import Product


class Cart(object):
    # Instantiate the cart
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = {}
            self.session.get(settings.CART_SESSION_ID) == cart

        self.cart = cart

    # Products in the cart
    def __iter__(self):
        for prod in self.cart.keys():
            self.cart[str(prod)]['product'] = Product.objects.get(pk=prod)

    # Length of the cart items(quantity)
    def __len__(self):
        return sum([item['quantity'] for item in self.cart.values()])

    def save(self):
        self.session(settings.CART_SESSION_ID) == self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        # Stringify product_id
        product_id = str(product_id)
        # Put product_id inside the cart
        if product_id not in self.cart:
            self.cart[product_id] = {'id': product_id, 'quantity': 1}
        # Updating quantity
        if update_quantity:
            self.cart[product_id] += int(quantity)
            # Remove the product_id if its value is 0
            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save
