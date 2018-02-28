
import numpy as np


def parseIn(path):
    with open(path, 'r') as f:
        dimensions = f.readline().strip().split()
        print(dimensions)
        for line in f:
            print(line.strip().split())

def parseOut(path, dimensions, array):
    with open(path, 'w') as f:
        header = ' '.join(str(dim) for dim in dimensions)
        np.savetxt(path, array, delimiter=' ', header=header, fmt='%d', comments='')
