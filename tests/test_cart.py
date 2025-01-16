import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def setUp(self):
        self.p1 = Product("Laptop", 1000, 5)
        self.p2 = Product("Headphones", 50, 20)
        self.p3 = Product("Mouse", 25, 10)

        self.cart = Cart()

        self.cart.add_product(self.p1, 2)  #(2 * 1000 = 2000€)
        # self.cart.add_product(self.p2, 4)  #(4 * 50 = 200€)
        # self.cart.add_product(self.p3, 5)
        


    def test_clear_cart(self):
         print("[Test] Testing clear cart...")
         self.cart.clear_cart()
         clear_quantite = 0
         self.assertEqual(sum(self.cart.items.values()), clear_quantite)
         print("[Test] Product passed.")