import sympy as sp

A = sp.Matrix([[ 1 , 2 , 3 ],[ 0 , 3 , 0 ] , [ 0 , 0 , 1 ]]) #a matrix 3*3

L = A.eigenvals()
V = A.eigenvects()

print("EigenValues:", L)
print("EigenVectors:", V)


