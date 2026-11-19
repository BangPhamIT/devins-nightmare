import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from challenges.legacy_checkout import checkout

class CheckoutTests(unittest.TestCase):
    def test_discount_does_not_affect_shipping(self):
        self.assertEqual(checkout(100, 10, 20), 90.0)

    def test_tiny_order_cannot_be_negative(self):
        self.assertEqual(checkout(0.5, 0, 0), 0.5)

    def test_regular_checkout(self):
        self.assertEqual(checkout(50, 5, 0), 55.0)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            checkout(100, 0, 120)

if __name__ == '__main__':
    unittest.main()
