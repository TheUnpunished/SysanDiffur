import numpy as np

def diffur(func, h, x0, y0, step_count):
    y = []
    y.append(y0)
    x_next = x0
    for i in range(0, step_count-1):
        x_next = x_next + h
        y_next = y[i] + h*func(y[i],x_next)
        y.append(y_next)
    return np.array(y)

def diffur_steps(func, x0, y0, x_max, step_count):
    h = (x_max - x0) / step_count
    y = []
    y.append(y0)
    x_next = x0
    for i in range(0, step_count-1):
        x_next = x_next + h
        y_next = y[i] + h*func(y[i],x_next)
        y.append(y_next)
    return np.array(y)

def diffur_params(func, params, h, x0, y0, step_count):
    y = []
    y.append(y0)
    x_next = x0
    for i in range(0, step_count-1):
        x_next = x_next + h
        y_next = y[i] + h*func(y[i],x_next, params)
        y.append(y_next)
    return np.array(y)

def diffur_steps_params(func, params, x0, y0, x_max, step_count):
    h = (x_max - x0) / step_count
    y = []
    y.append(y0)
    x_next = x0
    for i in range(0, step_count-1):
        x_next = x_next + h
        y_next = y[i] + h*func(y[i],x_next, params)
        y.append(y_next)
    return np.array(y)