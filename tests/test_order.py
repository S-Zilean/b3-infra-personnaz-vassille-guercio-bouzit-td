from cart import Cart
import unittest
from product import Product

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
