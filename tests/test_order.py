import unittest
from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def setUp(self):
        # Initialisation d'une instance de Cart pour les tests
        self.cart = Cart()
        self.laptop = Product(name="Laptop", price=1200.0, stock=5)
        self.mouse = Product(name="Mouse", price=25.0, stock=10)
        self.keyboard = Product(name="Keyboard", price=50.0, stock=8)

        self.cart.add_product(self.laptop, 2)
        self.cart.add_product(self.mouse, 4)
        self.cart.add_product(self.keyboard, 3)
        print("\n[Setup] Created a Cart instance with products for testing.")

    def test_calculate_total_without_tax_standard_rate(self):
        print("[Test] Testing Total Calculation Without Tax (Standard Rate)...")
        total_without_tax = self.cart.calculate_total_without_tax(20)  # 20% de taxe
        expected_total = self.cart.calculate_total() * (1 - 20 / 100)
        self.assertAlmostEqual(total_without_tax, expected_total, places=2)
        print(f"[Test] Total without tax: {total_without_tax:.2f}€ (Expected: {expected_total:.2f}€)")
        print("[Test] Total Calculation Without Tax passed.")

    def test_calculate_total_without_tax_zero_rate(self):
        print("[Test] Testing Total Calculation Without Tax (Zero Rate)...")
        total_without_tax = self.cart.calculate_total_without_tax(0)  # 0% de taxe
        expected_total = self.cart.calculate_total()
        self.assertAlmostEqual(total_without_tax, expected_total, places=2)
        print(f"[Test] Total without tax: {total_without_tax:.2f}€ (Expected: {expected_total:.2f}€)")
        print("[Test] Total Calculation Without Tax (Zero Rate) passed.")

    def test_calculate_total_without_tax_full_tax(self):
        print("[Test] Testing Total Calculation Without Tax (100% Tax Rate)...")
        total_without_tax = self.cart.calculate_total_without_tax(100)  # 100% de taxe
        self.assertAlmostEqual(total_without_tax, 0.0, places=2)
        print("[Test] Total Calculation Without Tax (100% Tax Rate) passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)
