import numpy as np
from io import StringIO


def getFileData(filename):
    with open(filename) as f:
        return f.read()


data = getFileData('workfile.txt')

result = np.genfromtxt(StringIO(data), delimiter=(6, 4, 6), dtype='int')
print(result)
