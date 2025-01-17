from cart import Cart

class Order:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        self.items = cart.items
        self.total = cart.calculate_total()
        self.status = "Pending"

    def place_order(self):
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        self.status = "Completed"
        return f"Order placed successfully! Total: {self.total:.2f}€"

    def view_order(self):
        return "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()]) + \
               f"\nTotal: {self.total:.2f}€\nStatus: {self.status}"

    def track_order(self):
        return f"Current order status: {self.status}"

    def update_order(self, product, new_quantity):
        if product in self.items:
            self.items[product] = new_quantity
            self.total = sum(p.price * q for p, q in self.items.items())
            return f"Order updated. New total: {self.total:.2f}€"
        return "Product not found in the order."
