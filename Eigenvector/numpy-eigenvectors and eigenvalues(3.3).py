import numpy as np

A = np.array([[ 1 , 2 , 3 ],[ 0 , 3 , 0 ] , [ 0 , 0 , 1 ]]) #a matrix 3*3

L , V = np.linalg.eig(A)

print("EigenValues:", L)
print("EigenVectors:", np.around(V , decimals=1))


