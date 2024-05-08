import numpy as np
import matplotlib.pyplot as plt 


# Vector values
a = np.array([10,15])
b = np.array ([15,20])

# Vector
plt.quiver (a[0],a[1] , angles='xy' , scale_units='xy' , scale=1)
plt.xlim ( -1 , 5)
plt.ylim ( 0 , 5)
plt.text ( a[0],a[1] , r'$\vec{u}$' , size=25 )
