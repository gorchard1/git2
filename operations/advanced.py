import math

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Остаток от деления на ноль")
    return a % b
