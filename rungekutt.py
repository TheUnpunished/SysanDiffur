import numpy as np

def diffur(func, h, x0, y0, step_count):
    y = []
    y.append(y0)
    x_next = x0
    for i in range(0, step_count-1):
        x_next = x_next + h
        k1 = func(y[i], x_next)
        k2 = func(y[i] + h * k1 / 2, x_next + h / 2)
        k3 = func(y[i] + h * k2 / 2, x_next + h / 2)
        k4 = func(y[i] + h * k3, x_next + h)
        y_delta = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y_next = y[i] + y_delta
        y.append(y_next)
    return np.array(y)


def diffur_steps(func, x0, y0, x_max, step_count):
    h = (x_max - x0) / step_count
    y = []
    y.append(y0)
    x_next = x0
    for i in range(0, step_count-1):
        x_next = x_next + h
        k1 = func(y[i], x_next)
        k2 = func(y[i] + h * k1 / 2, x_next + h / 2)
        k3 = func(y[i] + h * k2 / 2, x_next + h / 2)
        k4 = func(y[i] + h * k3, x_next + h)
        y_delta = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y_next = y[i] + y_delta
        y.append(y_next)
    return np.array(y)

def diffur_params(func, params, h, x0, y0, step_count):
    y = []
    y.append(y0)
    x_next = x0
    for i in range(0, step_count-1):
        x_next = x_next + h
        k1 = func(y[i], x_next, params)
        k2 = func(y[i] + h * k1 / 2, x_next + h / 2, params)
        k3 = func(y[i] + h * k2 / 2, x_next + h / 2, params)
        k4 = func(y[i] + h * k3, x_next + h, params)
        y_delta = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y_next = y[i] + y_delta
        y.append(y_next)
    return np.array(y)

def diffur_steps_params(func, params, x0, y0, x_max, step_count):
    h = (x_max - x0) / step_count
    y = []
    y.append(y0)
    x_next = x0
    for i in range(0, step_count-1):
        x_next = x_next + h
        k1 = func(y[i], x_next, params)
        k2 = func(y[i] + h * k1 / 2, x_next + h / 2, params)
        k3 = func(y[i] + h * k2 / 2, x_next + h / 2, params)
        k4 = func(y[i] + h * k3, x_next + h, params)
        y_delta = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y_next = y[i] + y_delta
        y.append(y_next)
    return np.array(y)