import numpy as np

ION_COUNT = 10000

if __name__ == "__main__":
    # Initialize
    ions = np.empty((ION_COUNT, 2), dtype = float)
    active = [True for _ in range(ION_COUNT)]
