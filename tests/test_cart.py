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
    
    def test_get_item_count(self):
        print("[Test] Testing Get Item Count...")
        self.cart.get_item_count()
        print("[Test] Get Item Count passed.")

    def test_clear_cart(self):
        print("[Test] Testing clear cart...")
        self.cart.clear_cart()
        clear_quantite = 0
        self.assertEqual(sum(self.cart.items.values()), clear_quantite)
        print("[Test] Clear cart passed.")
        


if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display printsimport unittest
