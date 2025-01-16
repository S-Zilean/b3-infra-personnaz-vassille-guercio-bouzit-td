import sys
import os
import unittest
# Ajoute le répertoire parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import Cart
from product import Product


class TestCart(unittest.TestCase):

    def setUp(self):
        # Initialisation d'une instance de Cart pour les tests
        self.cart = Cart()
        self.cart.add_product("Laptop", 1200.0, 2)
        self.cart.add_product("Mouse", 25.0, 4)
        self.cart.add_product("Keyboard", 50.0, 3)
        print("\n[Setup] Created a Cart instance with products for testing.")

    def test_cart_initialization(self):
        print("[Test] Testing Cart Initialization...")
        self.assertEqual(len(self.cart.products), 3)
        print("[Test] Cart Initialization passed.")

    def test_moyenne(self):
        print("[Test] Testing Cart Average Price Calculation...")
        moyenne = self.cart.moyenne()
        print(f"Prix moyen par produit dans le panier : {moyenne:.2f}€")
        expected_average = (1200.0 + 25.0 + 50.0) / 3
        self.assertAlmostEqual(moyenne, expected_average, places=2)
        print("[Test] Cart Average Price Calculation passed.")

    def test_empty_cart_moyenne(self):
        print("[Test] Testing Average Price for an Empty Cart...")
        empty_cart = Cart()
        moyenne = empty_cart.moyenne()
        self.assertEqual(moyenne, 0)
        print("[Test] Average Price for an Empty Cart passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)

