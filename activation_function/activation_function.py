import numpy as np
import matplotlib.pylab as plt

class ActivationFunction():

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

if __name__ == "__main__":
    activation_function = ActivationFunction()

    x = np.arange(-5.0, 5.0, 0.1)
    y = activation_function.sigmoid(x)

    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
