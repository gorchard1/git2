import math
import unittest

from operations.basic import add, sub, mul, div, sin, cos


class TestBasicOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(0, 5), 5)

    def test_sub(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 2), 3.5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0.0)
        self.assertAlmostEqual(sin(math.pi / 2), 1.0)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1.0)
        self.assertAlmostEqual(cos(math.pi), -1.0)


if __name__ == "__main__":
    unittest.main()