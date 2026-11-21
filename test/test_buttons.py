import unittest
from unittest.mock import patch, MagicMock

from main import Calculator


class TestButtonClicks(unittest.TestCase):
    def setUp(self):
        patcher_entry = patch("tkinter.Entry")
        patcher_button = patch("tkinter.Button")
        self.mock_entry = patcher_entry.start()
        self.mock_button = patcher_button.start()
        self.addCleanup(patcher_entry.stop)
        self.addCleanup(patcher_button.stop)

        self.root = MagicMock()
        self.calc = Calculator(self.root)

    def get_button_command(self, label):
        """Возвращает command для кнопки с указанным текстом."""
        for call in self.mock_button.call_args_list:
            _, kwargs = call
            if kwargs.get("text") == label:
                return kwargs.get("command")
        raise ValueError(f"Кнопка {label!r} не найдена")

    def click(self, label):
        """Эмулирует нажатие кнопки с указанным текстом."""
        self.get_button_command(label)()

    # ---------- Цифры и точка ----------

    def test_button_digit_click(self):
        self.click("7")
        self.assertEqual(self.calc.expr, "7")

        self.click("0")
        self.assertEqual(self.calc.expr, "70")

        self.click(".")
        self.assertEqual(self.calc.expr, "70.")

    # ---------- Базовые операции ----------

    def test_button_addition_click(self):
        self.click("2")
        self.click("+")
        self.click("3")
        self.click("=")
        self.assertEqual(self.calc.expr, "5.0")

    def test_button_subtraction_click(self):
        self.click("9")
        self.click("-")
        self.click("4")
        self.click("=")
        self.assertEqual(self.calc.expr, "5.0")

    def test_button_multiplication_click(self):
        self.click("6")
        self.click("*")
        self.click("7")
        self.click("=")
        self.assertEqual(self.calc.expr, "42.0")

    def test_button_division_click(self):
        self.click("8")
        self.click("/")
        self.click("2")
        self.click("=")
        self.assertEqual(self.calc.expr, "4.0")

    @patch("main.messagebox.showerror")
    def test_button_division_by_zero_click(self, mock_error):
        self.click("1")
        self.click("/")
        self.click("0")
        self.click("=")
        mock_error.assert_called_once()
        self.assertIn("Деление на ноль", mock_error.call_args[0][1])

    # ---------- Продвинутые операции ----------

    def test_button_mod_click(self):
        self.click("1")
        self.click("0")
        self.click("%")
        self.click("3")
        self.click("=")
        self.assertEqual(self.calc.expr, "1.0")

    def test_button_power_click(self):
        self.click("2")
        self.click("^")
        self.click("3")
        self.click("=")
        self.assertEqual(self.calc.expr, "8.0")

    def test_button_unary_sqrt_click(self):
        self.click("9")
        self.click("sqrt")
        self.assertEqual(self.calc.expr, "3.0")

    @patch("main.messagebox.showerror")
    def test_button_unary_sqrt_negative_click(self, mock_error):
        self.click("1")
        # "-4" через кнопки не собрать без =, поэтому сразу ставим expr
        self.calc.expr = "-4"
        self.click("sqrt")
        mock_error.assert_called_once()
        self.assertIn("Корень из отрицательного числа", mock_error.call_args[0][1])

    def test_button_unary_floor_click(self):
        self.click("3")
        self.click(".")
        self.click("7")
        self.click("floor")
        self.assertEqual(self.calc.expr, "3")

    def test_button_unary_ceil_click(self):
        self.click("3")
        self.click(".")
        self.click("2")
        self.click("ceil")
        self.assertEqual(self.calc.expr, "4")

    # ---------- Память ----------

    def test_button_memory_sequence_click(self):
        self.click("5")
        self.click("m+")
        self.assertEqual(self.calc.expr, "5.0")

        self.click("3")
        self.click("m-")
        self.assertEqual(self.calc.expr, "2.0")

        self.click("mr")
        self.assertEqual(self.calc.expr, "2.0")

        self.click("mc")
        self.assertEqual(self.calc.expr, "0.0")

    # ---------- Сброс и цепочки ----------

    def test_button_clear_click(self):
        self.click("5")
        self.click("+")
        self.click("3")
        self.click("C")
        self.assertEqual(self.calc.expr, "")

    def test_equals_single_number_click(self):
        self.click("4")
        self.click("2")
        self.click("=")
        self.assertEqual(self.calc.expr, "42")

    def test_full_expression_via_buttons(self):
        # (2 + 3) * 4 = 20
        self.click("2")
        self.click("+")
        self.click("3")
        self.click("=")
        self.assertEqual(self.calc.expr, "5.0")

        self.click("*")
        self.click("4")
        self.click("=")
        self.assertEqual(self.calc.expr, "20.0")

    # ---------- Проверка, что все кнопки из layout присутствуют ----------

    def test_all_buttons_created(self):
        expected = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "%", "^", "sqrt", "floor", "ceil", "sin", "cos",
            "m+", "m-", "mr", "mc",
            "C",
        ]
        created = [
            kwargs.get("text")
            for _, kwargs in self.mock_button.call_args_list
        ]
        for label in expected:
            self.assertIn(label, created, f"Кнопка {label!r} не создана")

    def test_all_buttons_have_command(self):
        for call in self.mock_button.call_args_list:
            _, kwargs = call
            self.assertIsNotNone(
                kwargs.get("command"),
                f"Кнопка {kwargs.get('text')!r} без command",
            )


if __name__ == "__main__":
    unittest.main()