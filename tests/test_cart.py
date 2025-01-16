import unittest
from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def setUp(self):
        # Setup instance for testing
        self.p1 = Product("Laptop", 1000, 5)
        self.p2 = Product("Headphones", 50, 20)
        self.p3 = Product("Mouse", 25, 10)

        self.cart = Cart()

        self.cart.add_product(self.p1, 2)  #(2 * 1000 = 2000€)
        self.cart.add_product(self.p2, 4)  #(4 * 50 = 200€)
        self.cart.add_product(self.p3, 5)

    # Pour executer le test, depuis la racine projet faire : python -m unittest tests/test_cart.py
    def test_mettre_de_cote(self):
        print("[Test] Testing mettre de cote...")
        self.cart.mettre_de_cote(self.p3)
        total_quantite = (2 + 4)
        self.assertEqual(sum(self.cart.items.values()), total_quantite)
        print("[Test] Mdc passed.")