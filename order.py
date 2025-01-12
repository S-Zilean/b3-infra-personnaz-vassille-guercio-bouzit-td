# order.py

from cart import Cart

class Order:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        self.items = cart.items
        self.total = cart.calculate_total()
        self.discount = 0

    def place_order(self):
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        return f"Order placed successfully! Total: {self.total:.2f}€"

    def view_order(self):
        return "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()]) + \
               f"\nTotal: {self.total:.2f}€"
    
    def discount_code(self, code: str):
        codes = {"SOLDE10": 0.1, "SOLDE20": 0.2}
        if code in codes:
            remise = codes[code]
            self.discount = self.total * remise
            self.total -= self.discount
            return f"Code apply successfully! Reduction: {self.discount:.2f}€"
        else:
            return "Code invalid"
