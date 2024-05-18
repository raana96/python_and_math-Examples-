import sympy as sp
import matplotlib.pyplot as plt 

x = sp.symbols('x')
f = (x ** 2-1) / (x-1)
o = sp.limit(f , x , 1)
print(f , "=" , o)

import numpy as np

x = sp.symbols('x')
x = np.linspace(0 , 2 ,10) 
y = (x ** 2-1) / (x-1)
plt.plot(x , y)
plt.axvline( x = 1 , color='r' , linestyle='--')
plt.axhline( y=2 , color='r' , linestyle='--')
plt.show()

