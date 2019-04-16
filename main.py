import math
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import mlab

# начальные условия
n = int(input('Введите число отрезков n = '))
x0 = 0
y0 = 0.1
xn = 1
h = (xn-x0)/n


x_list = np.linspace(0, 1, n + 1) # n отрезков, следовательно n + 1 точка
print(x_list)


def func(x, y):
    return 50 * y * (x-0.6) * (x-0.85)

def accurAnswer(x):
    return 0.1 * math.exp(50*pow(x, 3)/3 - 145*pow(x, 2)/4 + 25.5*x)


# массив со значениями точного решения
y_list = []
print("Точные значения в точках")
for x in x_list:
    y_list.append(round(accurAnswer(x), 5))


print(y_list)


def eiler(x, y, h, f):
    return y + h*f(x, y)


y = y0
y_list_eiler = [0.1]
print("Явный метод Эйлера для", n, "шагов")
for x in x_list:
    y = eiler(x, y, h, func)
    y_list_eiler.append(round(y, 5))


print(y_list_eiler[:n+1])


def runge_kutta(x, y, h, f):

    def k_1(x, y):
        return h * f(x, y)

    def k_2(x, y):
        return h * f(x + h/2, y + k_1(x, y)/2)

    def k_3(x, y):
        return h * f(x + h/2, y + k_2(x, y)/2)

    def k_4(x, y):
        return h * f(x + h, y + k_3(x, y))

    return y + k_1(x, y) / 6 + k_2(x, y) / 3 + k_3(x, y) / 3 + k_4(x, y) / 6

y = y0
y_list_runge = [0.1]
print("Метод Рунге-Кутта 4-го порядка для", n, "шагов")
for x in x_list:
    y = runge_kutta(x, y, h, func)
    y_list_runge.append(round(y, 5))


print(y_list_runge[:n+1])

print("Метод Симпсона для ", n, "шагов")


def simpson(x_list, y_list_eiler, h, f):
    prev = y_list_eiler[1]
    preprev = y_list_eiler[0]
    result_list = [preprev, prev]
    for i in range(0, n - 1):
        y = preprev + h * (f(x_list[i+2], y_list_eiler[i + 2]) + 4*f(x_list[i+1], prev) + f(x_list[i], preprev)) / 3
        preprev = prev
        prev = y
        result_list.append(round(y, 5))
    return result_list


y_list_simpson = simpson(x_list, y_list_eiler, h, func)


print(y_list_simpson)

plt.rc('font', **{'family': 'tahoma'})
plt.xlabel("abciss")
plt.ylabel("ordinat")
plt.plot(x_list, y_list, "c-", label=" accurate")
plt.plot(x_list, y_list_eiler[:n+1], "m-", label=" euler")
plt.plot(x_list, y_list_runge[:n+1], "y-", label=" runge")
plt.plot(x_list, y_list_simpson, "k-", label="simpson")

plt.legend()
plt.grid()
plt.show()
