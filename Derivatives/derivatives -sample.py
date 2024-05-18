import sympy as sp

x = sp.symbols('x')


f = x ** 2 - 6 * x + 5
d = sp.diff(f)
print(f ,"  d=" , d)
print(sp.solve(d))

import matplotlib.pyplot as plt 
import numpy as np

x = sp.symbols('x')
x = np.linspace(-4 , 10 ,100) 
y = x ** 2 - 6 * x + 5
plt.plot(x , y)
plt.axvline( x = 3 , color='r' , linestyle=':')
# x = 3
#x ** 2 - 6 * x + 5
#print(3 ** 2 - 6 * 3 + 5) # out = -4
plt.axhline( y= -4 , color='r' , linestyle=':')
plt.show()

