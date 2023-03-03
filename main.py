import numpy as np
import matplotlib.pyplot as plt


def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def exponential_fn(x):
    e_x = 1
    exponentials = []

    for i in range(1, 10):
        exponentials.append(e_x)
        e_xi = (np.power(x, i) / factorial(i))
        e_x += e_xi

    return exponentials


x = 1
plt.plot(exponential_fn(x))
plt.show()
