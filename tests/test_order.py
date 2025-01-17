from cart import Cart
import unittest
from product import Product

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

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.laptop = Product(name="Laptop", price=1200.0, stock=5)
        self.mouse = Product(name="Mouse", price=25.0, stock=10)
        self.keyboard = Product(name="Keyboard", price=50.0, stock=8)
        self.cart.add_product(self.laptop, 2)
        self.cart.add_product(self.mouse, 4)
        self.cart.add_product(self.keyboard, 3)
        self.order = Order(self.cart)

    def test_update_order(self):
        self.order.update_order(self.laptop, 1)
        self.assertEqual(self.order.items[self.laptop], 1)
        expected_total = sum(p.price * q for p, q in self.order.items.items())
        self.assertAlmostEqual(self.order.total, expected_total)

    def test_update_order_invalid_product(self):
        fake_product = Product(name="Fake", price=100.0, stock=1)
        result = self.order.update_order(fake_product, 1)
        self.assertEqual(result, "Product not found in the order.")

if __name__ == "__main__":
    unittest.main(buffer=False)
