import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

#Created By Raviv Herrera

x = sy.Symbol('x')
f = sy.cos(x)
print(f" f(x) = {f}")

xx = np.linspace(-10, 10, 100)
yy = np.ndarray(xx.size, dtype=np.float)
for i in range(len(xx)):
    yy[i] = f.subs(x, xx[i])


def B_section(epsilon, a, b, func, Mode):
    if Mode:
        plt.grid('on')
        plt.axis([-10, 10, -10, 10])
        plt.axhline()
        plt.axvline()
        plt.xlabel(" Y axis ", color='r')
        plt.ylabel(" X axis ", color='r')
        plt.plot(10, 10, 'w', label=f"Epsilon = {epsilon}")
        plt.plot(10, 10, 'w', label=f"f(a) = {func.subs(x, a)}")
        plt.plot(10, 10, 'w', label=f"f(b) = {func.subs(x, b)}")
        plt.plot(xx, yy, 'r', label=f" f(x) = {func}")
        plt.legend()
        CE = 1
        if (func.subs(x, a) > 0 and func.subs(x, b) > 0) or (func.subs(x, a) < 0 and func.subs(x, b) < 0):
            raise ValueError("f(a) and f(b) have the same sign")
        while CE > epsilon:
            c = (a + b) / 2.
            print(f" f(a) = {func.subs(x, a)} , f(b) = {func.subs(x, b)} , f(c) = {func.subs(x, c)}")
            plt.plot(c, 0, "*", color='magenta')
            plt.pause(1)
            if func.subs(x, c) == 0:
                plt.plot(c, 0, "*", color='orange')
                plt.text(-7.5, -5, f"Root = {c}")
                return c
            elif func.subs(x, a) * func.subs(x, c) < 0:
                b = c
            else:
                a = c
            CE = (b - a)
        plt.plot(c, 0, "*", color='orange')
        plt.text(-7.5, -5, f"Root ~ {c}")
        plt.show()
        return c
    else:
        CE = 1
        if (func.subs(x, a) > 0 and func.subs(x, b) > 0) or (func.subs(x, a) < 0 and func.subs(x, b) < 0):
            raise ValueError("f(a) and f(b) have the same sign")
        while CE > epsilon:
            c = (a + b) / 2.
            print(f" f(a) = {func.subs(x, a)} , f(b) = {func.subs(x, b)} , f(c) = {func.subs(x, c)}")
            if func.subs(x, c) == 0:
                return c
            elif func.subs(x, a) * func.subs(x, c) < 0:
                b = c
            else:
                a = c
            CE = (b - a)
        return c


alpha = B_section(0.01, 0, 2, f, True)
print(alpha)
