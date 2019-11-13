import numpy as np
from io import StringIO

data = u"\n".join(str(i) for i in range(10))

result = np.genfromtxt(StringIO(data), skip_header=1, skip_footer=6)
print(result)
