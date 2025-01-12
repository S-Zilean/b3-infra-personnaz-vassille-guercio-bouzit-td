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

    def test_get_item_count(self):
        print("[Test] Testing Get Item Count...")
        self.cart.add_product(self.product1, 7)
        self.cart.add_product(self.product2, 10)
        self.cart.get_item_count()
        print("[Test] Get Item Count passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints
import unittest
from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def setUp(self):
        self.p1 = Product("Laptop", 1000, 5)
        self.p2 = Product("Headphones", 50, 20)
        self.p3 = Product("Mouse", 25, 10)

        self.cart = Cart()

        self.cart.add_product(self.p1, 2)  #(2 * 1000 = 2000€)
        self.cart.add_product(self.p2, 4)  #(4 * 50 = 200€)
        self.cart.add_product(self.p3, 5)
        self.cart.mettre_de_cote(self.p3)

    # Pour executer le test, depuis la racine projet faire : python -m unittest tests/test_cart.py
    def test_mettre_de_cote(self):
        print("[Test] Testing mettre de cote...")
        total_quantite = (2 + 4)
        self.assertEqual(sum(self.cart.items.values()), total_quantite)
        print("[Test] Mdc passed.")