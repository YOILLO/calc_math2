import math


def get_function(num):
    if num == 1:
        return lambda x: x ** 3 - 3 * (x ** 2) + 1
    if num == 2:
        return lambda x: math.sin(x) - 0.2 * x + 1
    if num == 3:
        return lambda x: x ** 4 - 3 * (x ** 3) + 2.2
    if num == 4:
        return lambda x: math.atan(x) + x + 2


def string_function(num):
    if num == 1:
        return "x^3 - 3 * x^2 + 1"
    if num == 2:
        return "sin(x) - 0.2*x + 1"
    if num == 3:
        return "x^4 - 3x^3 + 2.2"
    if num == 4:
        return "arctan(x) + x  + 2"


def get_system_function(num):
    if num == 1:
        return lambda x, y: 0.1*(x**2) + x + 0.2 * (y**2) - 0.3
    if num == 2:
        return lambda x, y: 0.2*(x**2) + y - 0.1 * x * y - 0.2


def string_system_function(num):
    if num == 1:
        return "0.1*x^2 + x + 0.2 y^2 - 0.3"
    if num == 2:
        return "0.2*x^2 + y - 0.1 * x * y - 0.2"
