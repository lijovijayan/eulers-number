import numpy as np
import matplotlib.pyplot as plt


def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def taylor_expansion(x):
    exponential_sum = 1
    exponential_terms = []

    for i in range(1, 10):
        exponential_terms.append(exponential_sum)
        e_xi = (np.power(x, i) / factorial(i))
        exponential_sum += e_xi

    return exponential_terms


x = 1
plt.plot(taylor_expansion(x))
plt.show()
