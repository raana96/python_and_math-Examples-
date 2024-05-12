import numpy as np

A = np.array([[ 1 , 4],[ 3 , 2 ]]) #a matrix

L , V = np.linalg.eig(A)

print("EigenValues:", L)
print("EigenVectors:", np.around(V , decimals=1))

#AV = l*V

c = np.dot(A,V[:,0])
print(">>",c)