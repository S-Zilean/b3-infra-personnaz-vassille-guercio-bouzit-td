# cart.py

from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}
        self.mdc = {} # produit de coter

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())
   def moyenne(self):
        return self.calculate_total() / sum(quantity for product, quantity in self.items.items())

    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        return "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                          for product, quantity in self.items.items()])
    
    def get_item_count(self):
        print(f'il y a {sum(quantity for quantity in self.items.values())} produits dans votre panier')    
    
    def mettre_de_cote(self, product: Product):
        if product in self.items :
            quantity = self.items[product]
            self.mdc[product] = self.mdc.get(product, 0) + quantity
            del self.items[product]

    def clear_cart(self):
        for product in list(self.items.keys()) :
            del self.items[product]

