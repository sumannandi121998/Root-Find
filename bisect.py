from scipy.optimize import bisect
import numpy as np
def f(x):
   return (np.sin(np.cos(np.exp(x))))
root = bisect(f, -1, 1)
print (root)
