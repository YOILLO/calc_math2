import numpy as np

h = 0.000000001


def derivative(f):
    global h
    return lambda x: (f(x + h) - f(x - h)) / (2 * h)


def derivative_x(f):
    global h
    return lambda x, y: (f(x + h, y) - f(x - h, y)) / (2 * h)


def derivative_y(f):
    global h
    return lambda x, y: (f(x, y + h) - f(x, y - h)) / (2 * h)


def find_intervals(function):
    prev = -100
    intervals = []
    for i in np.arange(-100, 100, 0.5):
        try:
            if function(i) * function(prev) < 0:
                intervals.append((prev, i))
            prev = i
        except Exception:
            prev = i
            continue
    return intervals


def newton_method(function, a, b, error):
    x_prev = 0
    if function(a) * derivative(derivative(function))(a) > 0:
        x_prev = a
    else:
        x_prev = b
    x_current = x_prev
    x_prev = x_current * 1000 + 10
    iterations = 0
    while (abs(x_current - x_prev) > error) or (abs(function(x_current)) > error):
        x_prev = x_current
        iterations += 1
        x_current = x_prev - function(x_prev) / derivative(function)(x_prev)
    return x_current, iterations


def iterations_method(function, a, b, error):
    dev_a = derivative(function)(a)
    dev_b = derivative(function)(b)

    lyambd_a = -(1 / dev_a)
    lyambd_b = - (1 / dev_b)

    if (dev_a > dev_b):
        lyambd = lyambd_a
    else:
        lyambd = lyambd_b

    fi = lambda x: x + lyambd * function(x)

    x_current = a
    x_prev = a * 1000 + 10

    iterations = 0

    while (abs(x_prev - x_current) > error) or (abs(function(x_current)) > error):
        x_prev = x_current
        x_current = fi(x_prev)
        iterations += 1
        if iterations > 1000:
            print("Алгоритм расходится")
            break

    return x_current, iterations


def iterations_method_system(function1, function2, x, y, error):
    dev_x = derivative_x(function1)(x, y)
    dev_y = derivative_y(function2)(x, y)

    lyambd_x = -(1 / dev_x)
    lyambd_y = -(1 / dev_y)

    fi_x = lambda x, y: x + lyambd_x * function1(x, y)
    fi_y = lambda x, y: y + lyambd_y * function2(x, y)

    x_current = x
    x_prev = x * 1000 + 10

    y_current = y
    y_prev = y * 1000 + 10

    iterations = 0

    while max(abs(x_prev - x_current), abs(y_prev - y_current)) > error:
        x_prev = x_current
        y_prev = y_current
        x_current = fi_x(x_prev, y_prev)
        y_current = fi_y(x_prev, y_prev)
        iterations += 1
        if iterations > 1000:
            print("Алгоритм расходится")
            break

    return x_current, y_current, iterations
