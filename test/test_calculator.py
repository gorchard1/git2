import sys
import unittest
from unittest.mock import MagicMock

_tk_mock = MagicMock()
sys.modules["tkinter"] = _tk_mock
sys.modules["tkinter.messagebox"] = _tk_mock.messagebox

from main import Calculator


class TestCalculatorLogic(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator(MagicMock())
        self.calc.display = MagicMock()

    def test_digit_single(self):
        self.calc.digit("5")
        self.assertEqual(self.calc.expr, "5")

    def test_digit_multiple(self):
        self.calc.digit("1")
        self.calc.digit("2")
        self.calc.digit("3")
        self.assertEqual(self.calc.expr, "123")

    def test_digit_decimal_point(self):
        self.calc.digit("3")
        self.calc.digit(".")
        self.calc.digit("14")
        self.assertEqual(self.calc.expr, "3.14")

    def test_set_op(self):
        self.calc.digit("5")
        self.calc.set_op("+")
        self.assertEqual(self.calc.expr, "5 + ")

    def test_clear(self):
        self.calc.digit("5")
        self.calc.clear()
        self.assertEqual(self.calc.expr, "")

    def test_equals_addition(self):
        self.calc.expr = "2 + 3"
        self.calc.equals()
        self.assertEqual(self.calc.expr, "5.0")

    def test_equals_multiplication(self):
        self.calc.expr = "4 * 5"
        self.calc.equals()
        self.assertEqual(self.calc.expr, "20.0")

    def test_equals_division(self):
        self.calc.expr = "10 / 4"
        self.calc.equals()
        self.assertEqual(self.calc.expr, "2.5")

    def test_unary_sqrt(self):
        self.calc.expr = "9"
        self.calc.unary("sqrt")
        self.assertEqual(self.calc.expr, "3.0")

    def test_unary_sin_zero(self):
        self.calc.expr = "0"
        self.calc.unary("sin")
        self.assertEqual(self.calc.expr, "0.0")

    def test_mem_m_plus_and_mr(self):
        self.calc.expr = "5"
        self.calc.mem("m_plus")
        self.calc.expr = ""
        self.calc.mem("mr")
        self.assertEqual(self.calc.expr, "5.0")

    def test_mem_mc(self):
        self.calc.expr = "5"
        self.calc.mem("m_plus")
        self.calc.mem("mc")
        self.calc.expr = ""
        self.calc.mem("mr")
        self.assertEqual(self.calc.expr, "0.0")


if __name__ == "__main__":
    unittest.main()
