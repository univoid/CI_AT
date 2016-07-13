import matplotlib.pyplot as plt


def draw_rect(l):
    plt.scatter(*zip(*l))
    plt.show()
