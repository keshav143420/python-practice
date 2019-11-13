import numpy as np
from io import StringIO

# data = u"1, abc , 2\n 3, xxx, 4"
# # Without autostrip
# result = np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5")
# print(result)
# # With autostrip
# result = np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5", autostrip=True)
# print(result)


data = u"""QQ
QQ Skip me !
QQ Skip me too !
1, 2
3, 4
5, 6 QQThis is the third line of the data
7, 8
QQ And here comes the last line
9, 0
"""
result = np.genfromtxt(StringIO(data), comments="QQ", delimiter=",")
print(result)

