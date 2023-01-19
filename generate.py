import numpy as np
import random
import matplotlib.pyplot as plt

ION_COUNT = 10000
START_X = 0
START_Y = 0
STOP_X = 10
STOP_Y = 10
ION_MOVEMENT = 0.05

def move(ions, active):
    for i in range(ION_COUNT):
        if active[i]:
            for j in range(2):
                ions[i][j] += random.uniform(-ION_MOVEMENT, ION_MOVEMENT)
    ions[:,0] = np.clip(ions[:,0], START_X, STOP_X)
    ions[:,1] = np.clip(ions[:,1], START_Y, STOP_Y)

def draw(ions, active):
    plt.scatter(ions[:,0], ions[:,1], 1, c=active[:])
    plt.xlim(START_X, STOP_X)
    plt.ylim(START_Y, STOP_Y)
    plt.pause(0.001)
    plt.clf()

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

    for i in range(100):
        move(ions, active)
        draw(ions, active)
