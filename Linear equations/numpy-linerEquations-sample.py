import numpy as np

# 2x + 3y = 7 
# 3x + 4y = 9

A = np.array([[ 2 , 3],[ 3 , 4 ]])
b = np.array([7 , 9])

c = np.linalg.inv(A).dot(b)
print(c)

import matplotlib.pyplot as plt

x = np.linspace(-5,5,10)
y1 = ((2*x)-7) / 3
y2 = ((3*x)-9) / 4
plt.plot(x , y1)
plt.plot(x,y2)
plt.show()
