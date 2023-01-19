import numpy as np
import random
import matplotlib.pyplot as plt

ION_COUNT = 10000
START_X = 0
START_Y = 0
STOP_X = 10
STOP_Y = 10

def draw(ions, active):
    plt.scatter(ions[:,0], ions[:,1], 1, c=active[:])
    plt.xlim(START_X, STOP_X)
    plt.ylim(START_Y, STOP_Y)
    plt.show()

if __name__ == "__main__":
    # Initialize
    ions = np.empty((ION_COUNT, 2), dtype = float)
    active = [True for _ in range(ION_COUNT)]

    # Put ions in random positions
    for i in range(ION_COUNT):
        ions[i] = [random.uniform(START_X, STOP_X), random.uniform(START_Y, STOP_Y)]

    # Tree starting point
    active[0] = False
    ions[0][0] = (STOP_X - START_X) / 2
    ions[0][1] = (STOP_Y - START_Y) / 2

    draw(ions, active)
