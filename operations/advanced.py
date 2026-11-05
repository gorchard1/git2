import math

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Остаток от деления на ноль")
    return a % b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Корень из отрицательного числа")
    return math.sqrt(a)

def floor(a):
    return math.floor(a)

def ceil(a):
    return math.ceil(a)

OPERATIONS = {
    '%': mod,
    '^': power,
    'sqrt': sqrt,
    'floor': floor,
    'ceil': ceil,
}
