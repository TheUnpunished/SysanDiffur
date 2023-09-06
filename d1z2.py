import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import eiler
import rungekutt

def model(x,t,params):
    k  = - math.log1p(((params[0]-params[1])/(params[2]-params[1])) ** (1/params[3]) - 1)
    dxdt = -k * (x-params[1])
    return dxdt

def func(t, params, x0):
    return params[1] + (x0-params[1]) * (((params[0]-params[1])/(params[2]-params[1])) ** (t/params[3]))
x0 = 100 # т. тела в начале наблюдения
t_min = 0 # начальный момент времени
t_max = 40 # конечный момент времени (график)
params = []
params.append(60) # т. тела в конце наблюдения
params.append(20) # т. воздуха
params.append(x0) # т. тела в начале наблюдения
params.append(20) # конечный момент времени (наблюдение)
step_count = 150
t = np.linspace(t_min,t_max,step_count)
# y = odeint(model, x0, t)
fun_values = []
for t_i in t:
    fun_values.append(func(t_i, params, x0))
fun_values = np.array(fun_values)
y1 = eiler.diffur_steps_params(model, params, t_min, x0, t_max, step_count)
y2 = rungekutt.diffur_steps_params(model, params, t_min, x0, t_max, step_count)
# plt.plot(t, y, 'b-', linewidth=2, label='Численный метод')
plt.step(t, y1, 'g-', linewidth=2, label='Метод Эйлера')
plt.step(t, y2, 'y-', linewidth=2, label='Метод Рунге-Кутты')
plt.plot(t, fun_values, 'r--', linewidth=2, label='Конечная функция')
plt.legend()
plt.xlabel('время')
plt.ylabel('x(t)')
plt.show()