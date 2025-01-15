import sys
import os
import unittest

# Ajoute le répertoire parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def setUp(self):
        # Setup a Cart instance for testing
        self.cart = Cart()
        self.product1 = Product(name="Apple", price=1.0, stock=10)
        self.product2 = Product(name="Banana", price=0.5, stock=20)
        print("\n[Setup] Created a Cart instance for testing.")

    def test_product_initialization(self):
        print("[Test] Testing Product Initialization...")
        self.assertEqual(self.product1.name, "Apple")
        self.assertEqual(self.product1.price, 1.0)
        self.assertEqual(self.product1.stock, 10)
        print("[Test] Product Initialization passed.")

    def test_get_item_count(self):
        print("[Test] Testing Get Item Count...")
        self.cart.add_product(self.product1, 3)
        self.cart.add_product(self.product2, 2)
        item_count = self.cart.get_item_count()
        self.assertEqual(item_count, 5)
        print("[Test] Get Item Count passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints
