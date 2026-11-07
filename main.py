import tkinter as tk
from tkinter import messagebox

from operations import ALL_OPERATIONS, Memory


class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Калькулятор")
        self.expr = ""
        self.memory = Memory()
        self.operations = ALL_OPERATIONS

        self.display = tk.Entry(root, font=("Consolas", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self._build_buttons()

    def _build_buttons(self):
        layout = [
            # цифры и базовые операции
            ("7", lambda: self.digit("7")), ("8", lambda: self.digit("8")),
            ("9", lambda: self.digit("9")), ("/", lambda: self.set_op("/")),
            ("4", lambda: self.digit("4")), ("5", lambda: self.digit("5")),
            ("6", lambda: self.digit("6")), ("*", lambda: self.set_op("*")),
            ("1", lambda: self.digit("1")), ("2", lambda: self.digit("2")),
            ("3", lambda: self.digit("3")), ("-", lambda: self.set_op("-")),
            ("0", lambda: self.digit("0")), (".", lambda: self.digit(".")),
            ("=", self.equals),            ("+", lambda: self.set_op("+")),
            # продвинутые операции
            ("%", lambda: self.set_op("%")),
            ("^", lambda: self.set_op("^")),
            ("sqrt", lambda: self.unary("sqrt")),
            ("floor", lambda: self.unary("floor")),
            ("ceil", lambda: self.unary("ceil")),
            ("sin", lambda: self.unary("sin")),
            ("cos", lambda: self.unary("cos")),
            # память
            ("m+", lambda: self.mem("m_plus")),
            ("m-", lambda: self.mem("m_minus")),
            ("mr", lambda: self.mem("mr")),
            ("mc", lambda: self.mem("mc")),
            # сброс
            ("C", self.clear),
        ]
        for i, (label, cmd) in enumerate(layout):
            row = 1 + i // 4
            col = i % 4
            tk.Button(self.root, text=label, command=cmd,
                      font=("Consolas", 14), width=6, height=2
                      ).grid(row=row, column=col, sticky="nsew")
        for c in range(4):
            self.root.grid_columnconfigure(c, weight=1)

    def digit(self, d):
        self.expr += d
        self._show()

    def set_op(self, op):
        self.expr += f" {op} "
        self._show()

    def unary(self, name):
        try:
            v = float(self.expr)
            self.expr = str(self.operations[name](v))
            self._show()
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def equals(self):
        try:
            t = self.expr.split()
            if len(t) == 3:
                a, op, b = float(t[0]), t[1], float(t[2])
                self.expr = str(self.operations[op](a, b))
                self._show()
            elif len(t) == 1:
                self.expr = t[0]
                self._show()
            else:
                raise ValueError("Неверное выражение")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def mem(self, cmd):
        try:
            value = float(self.expr) if self.expr else 0.0
            self.expr = str(getattr(self.memory, cmd)(value))
            self._show()
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def clear(self):
        self.expr = ""
        self._show()

    def _show(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expr)


if __name__== "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
