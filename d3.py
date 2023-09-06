import math
import time
import turtle

import matplotlib.pyplot as plt
import numpy as np


# param 0 - масса, m
# param 1 - коэфф. сопротивления, k
# param 2 - ускорение свободного падения, g


# S=m/k*ln(ch((kg/m)^0.5*t))

def model_final(t, params, v0):
    S_path = (params[0] / params[1]) * math.log1p(math.cosh(math.sqrt(params[1] * params[2] / params[0]) * t) - 1)
    return S_path


# 0 - Сфера
# 1 - Конус 2:1 (острием к потоку)
# 2 - Куб (поверхностью к потоку)
# 3 - Цилиндр (длина равна двум диаметрам, торцом к потоку)
# 4 - Вытянутое каплевидное тело
csf = [0.47, 0.50, 1.05, 0.82, 0.04]
csf_index = 2

# плотность вещества, в котором находится тело
ro = 1.2754

# сопротивляемая поверхность тела
S_area = 0.0002
k = 0.5 * ro * csf[csf_index] * S_area

# начальная скорость
v0 = 0
# начальное расстояние
s0 = 0

# начальный момент времени, сек
t_min = 0
# конечный момент времени
t_max = 60
# количество промежутков
step_count = 2500

# param 0 - масса, m
# param 1 - коэфф. сопротивления, k
# param 2 - ускорение свободного падения, g
params = [2, k, 100]

t = np.linspace(t_min, t_max, step_count)
fun_values = []

for t_i in t:
    fun_values.append(model_final(t_i, params, v0))
fun_values = np.array(fun_values)

plt.plot(t, fun_values, 'r--', linewidth=2, label='Конечная функция')
plt.legend()
plt.xlabel('время')
plt.ylabel('x(t)')
plt.show()

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Свободное падение тела с сопротивлением")

offset = 300

item = turtle.Turtle()
item.shape("circle")
item.color("red")
item.penup()
item.speed(0)
item.goto(0, offset)


count = 1
for fun_value in fun_values:
    item.goto(0, offset * count - fun_value * 10)
    time.sleep(t[1] - t[0])
    if item.ycor() < -300:
        count += 2.5

wn.mainloop()