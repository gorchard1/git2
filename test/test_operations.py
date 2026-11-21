import unittest

from operations import ALL_OPERATIONS, Memory


class TestAllOperations(unittest.TestCase):
    def test_contains_basic(self):
        for key in ["+", "-", "*", "/"]:
            self.assertIn(key, ALL_OPERATIONS, f"Отсутствует ключ '{key}'")

    def test_contains_trig(self):
        for key in ["sin", "cos"]:
            self.assertIn(key, ALL_OPERATIONS)

    def test_contains_advanced(self):
        for key in ["%", "^", "sqrt"]:
            self.assertIn(key, ALL_OPERATIONS)

    def test_contains_rounding(self):
        for key in ["floor", "ceil"]:
            self.assertIn(key, ALL_OPERATIONS)

    def test_all_are_callable(self):
        for name, op in ALL_OPERATIONS.items():
            self.assertTrue(callable(op), f"'{name}' не вызывается")

    def test_memory_class_importable(self):
        m = Memory()
        self.assertTrue(hasattr(m, "m_plus"))
        self.assertTrue(hasattr(m, "mr"))

    def test_integration_expression(self):
        # (2 + 3) * 4 = 20 — проверка, что операции комбинируются
        result = ALL_OPERATIONS["*"](ALL_OPERATIONS["+"](2, 3), 4)
        self.assertEqual(result, 20)


if __name__ == "__main__":
    unittest.main()
