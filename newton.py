from scipy.optimize import newton
import numpy as np
def f(x):
   return (np.sin(np.cos(np.exp(x))))
root1 = newton(f,-1)
root2 = newton(f,-0.1)
print ('The one root of the given eq',root1)
print ('The another root of the given eq',root2)

