import sys
import os
import unittest

# Ajoute le répertoire parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import Cart
from product import Product
from order import Order


class TestCart(unittest.TestCase):

    def setUp(self):
        # Setup a Cart instance for testing
        self.cart = Cart()
        self.product1 = Product(name="Apple", price=1.0, stock=10)
        self.product2 = Product(name="Banana", price=0.5, stock=20)
        self.cart.add_product(self.product1, quantity=3)
        self.cart.add_product(self.product2, quantity=8)

        print("\n[Setup] Created a Cart instance for testing.")

    def test_generate_receipt(self):
      print("[Test] Testing generate_receipt...")
      self.order = Order(self.cart)
      self.order.generate_receipt()
      print("[Test] Get generate_receipt passed.")


if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints
