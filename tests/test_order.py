import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import Cart
from product import Product
from order import Order

class TestCart(unittest.TestCase):

    def setUp(self):
        self.p1 = Product("Laptop", 1000, 5)
        self.p2 = Product("Headphones", 50, 20)
        self.p3 = Product("Mouse", 25, 10)

        self.cart = Cart()

        self.cart.add_product(self.p1, 2)  #(2 * 1000 = 2000€)

        self.order = Order(self.cart)

        self.order.place_order()

    def test_cancel_order(self):
        print("[Test] Testing cancel_order...")
        self.order.cancel_order()
        self.assertEqual(self.p1.stock, 5)
        print("[Test] cancel_order passed.")

if __name__ == "__main__":
    unittest.main()