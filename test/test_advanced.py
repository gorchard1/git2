import unittest

from operations.advanced import mod, power, sqrt, floor, ceil


class TestAdvancedOperations(unittest.TestCase):
    def test_mod(self):
        self.assertEqual(mod(10, 3), 1)
        self.assertEqual(mod(5, 5), 0)

    def test_mod_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            mod(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3.0)
        self.assertAlmostEqual(sqrt(2), 1.41421356237, places=6)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_floor(self):
        self.assertEqual(floor(3.7), 3)
        self.assertEqual(floor(-1.2), -2)

    def test_ceil(self):
        self.assertEqual(ceil(3.2), 4)
        self.assertEqual(ceil(-1.8), -1)


if __name__ == "__main__":
    unittest.main()