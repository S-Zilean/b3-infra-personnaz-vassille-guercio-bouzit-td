import sys
import os
import unittest

# Ajoute le répertoire parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import Cart
from product import Product
from order import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.p1 = Product("Laptop", 1000, 5)
        self.p2 = Product("Headphones", 50, 20)
        self.p3 = Product("Mouse", 25, 10)

        self.cart = Cart()

        self.cart.add_product(self.p1, 2)  #(2 * 1000 = 2000€)
        self.cart.add_product(self.p2, 4)  #(4 * 50 = 200€)

        self.order = Order(self.cart) # 2200€
        
        print("\n[Setup] Created a Cart instance for testing.")

    # Pour executer le test, depuis la racine projet faire : python -m unittest tests/test_order.py
    def test_discount_code(self):
        print("[Test] Discount order...")
        self.order.discount_code("SOLDE10")
        total = 2200 - (2200 * 0.1)
        self.assertEqual(self.order.total, total)
        print(f'{self.order.total}')
        self.test_generate_receipt()
        print("[Test] Discount order passed.")
    
    def test_generate_receipt(self):
      print("[Test] Testing generate_receipt...")
      self.order.generate_receipt()
      print("[Test] Get generate_receipt passed.")

    def test_cancel_order(self):
        print("[Test] Testing cancel_order...")
        self.order.cancel_order()        
        self.assertEqual(self.p1.stock, 7)
        print("[Test] cancel_order passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints
