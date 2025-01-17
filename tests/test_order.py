import sys
import os
import unittest

# Ajoute le répertoire parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import Cart
import unittest
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

    def test_discount_code(self):
        print("[Test] Discount order...")
        self.order.discount_code("SOLDE10")
        total = 2200 - (2200 * 0.1)
        self.assertEqual(self.order.total, total)
        print("[Test] Discount order passed.")
    
    def test_generate_receipt(self):
        print("[Test] Testing generate_receipt...")
        self.order.generate_receipt()
        print("[Test] Get generate_receipt passed.")
        
    def test_update_order(self):
        self.order.update_order(self.laptop, 1)
        self.assertEqual(self.order.items[self.laptop], 1)
        expected_total = sum(p.price * q for p, q in self.order.items.items())
        self.assertAlmostEqual(self.order.total, expected_total)

    def test_cancel_order(self):
        print("[Test] Testing cancel_order...")
        self.order.cancel_order()        
        self.assertEqual(self.p1.stock, 7)
        print("[Test] cancel_order passed.")

    def test_update_order_invalid_product(self):
        fake_product = Product(name="Fake", price=100.0, stock=1)
        result = self.order.update_order(fake_product, 1)
        self.assertEqual(result, "Product not found in the order.")

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints
