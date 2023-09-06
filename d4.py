import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# 0 - alpha, вероятность размножения травоядных
# 1 - beta, вероятность того, что травоядное будет съедено хищником
# 2 - gamma, вероятность того, что хищник умрёт от голода
# 3 - delta, вероятность того, что хищнику хватит еды на дальнейшее размножение

def dX_dt(X, t, params):
    dx_dt = params[0] * X[0] - params[1] * X[0] * X[1]
    dy_dt = - params[2] * X[1] + params[1] * params[3] * X[0] * X[1]
    return np.array([dx_dt, dy_dt])


def d2X_dt2(X, t, params):
    d2x_dt2 = [params[0] - params[1] * X[1],
               -params[1] * X[0]]
    d2y_dt2 = [params[1] * params[3] * X[1], -params[2] + params[1] * params[3] * X[0]]
    return np.array([d2x_dt2, d2y_dt2])


# 0 - alpha, вероятность размножения травоядных
# 1 - beta, вероятность того, что травоядное будет съедено хищником
# 2 - gamma, вероятность того, что хищник умрёт от голода
# 3 - delta, вероятность того, что хищнику хватит еды на дальнейшее размножение

params = np.array([0.3, 0.28, 0.7, 0.3])

t = np.linspace(0, 60, 10000)

# 10 кроливов, 5 лис
X0 = np.array([10.0, 5.0])
Y1 = odeint(dX_dt, y0=X0, t=t, args=(params,))

array = Y1.T

plt.plot(t, array[0], 'y-', linewidth=2, label='Кролики')
plt.plot(t, array[1], 'r--', linewidth=2, label='Лисы')
plt.legend()
plt.xlabel('Время, лет')
plt.ylabel('Численность')
plt.show()
