"""
y = x ** 2

dy/dx = 2 * x

x0 = 10

r = 0.2

iteration1 : x1 = x0 - r * d 
                = 10 - 0.2 * (2*10)
                = 6
                
iteration2 : x2 = x1 - r * d = 6     - 0.2 * (2*6)     = 3.59

iteration3 : x3 = x2 - r * d = 3.59  - 0.2 * (2*3.59)  = 2.159

iteration4 : x4 = x3 - r * d = 2.154 - 0.2 * (2*2.154) = 1.29
...
"""

import numpy as np

def gradient_descent(gradient, start, rate, n_iter):
    s = start
    for i in range(n_iter):
        a = -rate * gradient(s)
        if np.all(np.abs(a) <= 1e-06):
            break
        s += a
    return s

g = lambda x: 2 * x

r = gradient_descent(gradient=g, start=10.0, rate=0.2, n_iter=25)
print("rate=0.2")
print(r)

print("*****")
#

"""r = 0.8

iteration1 : x1 = x0 - r * d = 10    - 0.8 * (2*10)    = -6

iteration2 : x2 = x1 - r * d = -6    - 0.8 * (2*-6)    = 3.6

iteration3 : x3 = x2 - r * d = 3.6   - 0.8 * (2*3.6)   = -2.16

iteration4 : x4 = x3 - r * d = -2.16 - 0.8 * (2*-2.16) = 1.29
...
"""

r = gradient_descent(gradient=g, start=10.0, rate=0.8, n_iter=25)
np.round(r)
print("rate=0.8")
print(r)

print("*****")
"""r = 0.005

iteration1 : x1 = x0 - r * d = 10    - 0.005 * (2*10)    = 9.9

iteration2 : x2 = x1 - r * d = 9.9   - 0.005 * (2*9.9)   = 9.801

iteration3 : x3 = x2 - r * d = 9.801 - 0.005 * (2*9.801) = 9.70

iteration4 : x4 = x3 - r * d = 9.70  - 0.005 * (2*-9.70) = 9.6
    ...
"""

r = gradient_descent(gradient=g, start=10.0, rate=0.005, n_iter=25)
print("rate=0.005")
print(r)

r = gradient_descent(gradient=g, start=10.0, rate=0.005, n_iter=100)
np.round(r)
print(r)
r = gradient_descent(gradient=g, start=10.0, rate=0.005, n_iter=200)
np.round(r)
print(r)
r = gradient_descent(gradient=g, start=10.0, rate=0.005, n_iter=300)
np.round(r)
print(r)
# f(x,y) = x**2 + y**4

g = lambda x: np.array([2 * x[0], 
                        4 * x[1]**3])

gradient_descent(gradient=g, start=np.array([1.0, 1.0]), rate=0.2, n_iter=50)