from cart import Cart

class Order:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        self.items = cart.items
        self.total = cart.calculate_total()
        self.discount = 0
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
    
    def discount_code(self, code: str):
        codes = {"SOLDE10": 0.1, "SOLDE20": 0.2}
        if code in codes:
            remise = codes[code]
            self.discount = self.total * remise
            self.total -= self.discount
            return f"Code apply successfully! Reduction: {self.discount:.2f}€"
        else:
            return "Code invalid"
        
    def generate_receipt(self):
        receipt = "Order Receipt:\n"
        receipt += "\n".join([f"{product.name} x {quantity} - {product.price * quantity:.2f}€" for product, quantity in self.items.items()])
        receipt += f"\nTotal: {self.total:.2f}€"
        print(f'{receipt}')

    def cancel_order(self):
        #Annule la commande en restaurant les stocks et réinitialisant les articles.
        for product, quantity in self.items.items():
            product.stock += quantity  # Restaure les quantités en stock
        self.items.clear()  # Vide les articles de la commande
        self.total = 0  # Réinitialise le total de la commande
        return f"Order cancelled and stock restored successfully!"  
    
    def discount_code(self, code: str):
        codes = {"SOLDE10": 0.1, "SOLDE20": 0.2}
        if code in codes:
            remise = codes[code]
            self.discount = self.total * remise
            self.total -= self.discount
            return f"Code apply successfully! Reduction: {self.discount:.2f}€"
        else:
            return "Code invalid"
