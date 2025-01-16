# order.py

from cart import Cart

class Order:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        self.items = cart.items
        self.total = cart.calculate_total()

    def place_order(self):
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        return f"Order placed successfully! Total: {self.total:.2f}€"

    def view_order(self):
        return "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()]) + \
               f"\nTotal: {self.total:.2f}€"

    def cancel_order(self):
     #"""Annule la commande en restaurant les stocks et réinitialisant les articles."""
        for product, quantity in self.items.items():
            product.stock += quantity  # Restaure les quantités en stock
        self.items.clear()  # Vide les articles de la commande
        self.total = 0  # Réinitialise le total de la commande
        return f"Order cancelled and stock restored successfully!"