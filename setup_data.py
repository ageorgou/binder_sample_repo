import os

import numpy as np


def make_data(ncols=2, size=1000):
    """Create some random data of the given shape."""
    shape = (size, ncols)
    return np.random.randn(*shape)


def store_data(data):
    """Store the given data."""
    location = '.'
    out_file = os.path.join(location, 'data.csv')
    np.savetxt(out_file, data,
               fmt='%.5f', delimiter=',')


if __name__ == "__main__":
    np.random.seed(17)
    my_data = make_data()
    store_data(my_data)
