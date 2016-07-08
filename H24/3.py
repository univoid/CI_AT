import numpy as np
import matplotlib.pyplot as plt


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.ylim(0, 30)
    plt.xlim(0, 30)
    plt.plot(x, y)
    plt.show()


a = 0.5
b = 10
graph("{a} * x + {b}".format(a=a, b=b), range(0, 30))