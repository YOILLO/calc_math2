from calculations import *
from functions import *


def one_function():
    for i in range(4):
        print(f"{i + 1}: {string_function(i + 1)}")

    function_num = 0

    while function_num < 1 or function_num > 4:
        try:
            function_num = int(input("Введите номер функции которую хотите выбрать: "))
        except Exception:
            print("Введите число")

    print(f"Выбрана функция {string_function(function_num)}")

    function = get_function(function_num)

    intervals = find_intervals(function)

    print(f"Найденные приближения: {intervals}")
    print()

    for a, b in intervals:
        print(f"Вычисляю корень на приближении {a}, {b}")

        root_newton, iterations_newton = newton_method(function, a, b, 0.01)

        print(f"Методом ньютона найден корень {root_newton} за {iterations_newton} итераций")

        iteration_root, iterations_iteration = iterations_method(function, a, b, 0.01)

        print(f"Методом итераций найден корень {iteration_root} за {iterations_iteration} итераций")

        print(f"Разница между корнями: {abs(root_newton - iteration_root)}")

        print()


def two_functions():
    function1_num = 1
    function2_num = 2

    print(f"Выбранные функции: {string_system_function(function1_num)}, {string_system_function(function2_num)}")

    function1 = get_system_function(function1_num)
    function2 = get_system_function(function2_num)

    x_start = 0
    y_start = 1

    x_answer, y_answer, iterations = iterations_method_system(function1, function2, x_start, y_start, 0.001)

    print(f"Ответ x = {x_answer}, y = {y_answer}, получен за {iterations} итераций")


mode = 0

while mode < 1 or mode > 2:
    try:
        mode = int(input("Введите 1 для поиска корня уравнения, 2 для решения системы уравнений: "))
    except Exception:
        print("Введите число")

if mode == 1:
    one_function()
else:
    two_functions()
