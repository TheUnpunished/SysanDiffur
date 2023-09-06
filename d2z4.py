import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import eiler
import rungekutt

def model(x,t,r):
    dxdt = r * x * math.cos(t)
    return dxdt

def x_t(x0, t, r):
    return x0 * math.e ** (r * math.sin(t))

x0 = 100 # начальная популяция
t_min = 0 # начало отсчёта
t_max = 5 * math.pi # конец отсчёта
step_count = 100 # количество шагов
t = np.linspace(t_min,t_max,step_count)
r = 0.5 # коэффициент r  из задачи
y = odeint(model, x0, t, args=(r,))
# y1 = eiler.diffur_steps_params(model, r, t_min, x0, t_max, step_count)
y2 = rungekutt.diffur_steps_params(model, r, t_min, x0, t_max, step_count)
fun_values = []
for t_i in t:
    fun_values.append(x_t(x0, t_i, r))
plt.step(t, y, 'b-', linewidth=2, label='Численный метод')
# plt.step(t, y1, 'g-', linewidth=2, label='Метод Эйлера')
plt.step(t, y2, 'y-', linewidth=2, label='Метод Рунге-Кутты')
plt.plot(t, fun_values, 'r--', linewidth=2, label='Конечная функция')
plt.legend()
plt.xlabel('время (лет)')
plt.ylabel('x(t)')
plt.show()