import numpy as np
import matplotlib.pyplot as plt 


# Vector values
a = np.array([10,15])
b = np.array ([20,20])
print ( a , b)

# Vector
plt.quiver (a[0],a[1] , angles='xy' , scale_units='xy' , scale=1)
plt.xlim ( -10 , 20)
plt.ylim ( -10, 20)

plt.text ( a[0],a[1] , r'$\vec{a}$' , size=25 )

plt.quiver (b[0],b[1] , angles='xy' , scale_units='xy' , scale=1)
plt.text ( b[0],b[1] , r'$\vec{b}$' , size=25 )

#OP
c = a - b
print ( c)

plt.quiver ( c[0],c[1] , angles='xy' , scale_units='xy' , scale=1, color="red" )
plt.text ( c[0],c[1] , r'$\vec{c}$' , size=25 )

plt.show()