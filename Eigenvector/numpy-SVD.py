import numpy as np

A = np.array([[ 3 , 1 , 1 ],[ -1 , 3 , 1 ]]) #a matrix

At = A.T

#np.dot(A,At)
#np.dot(At,A)

U,S,Vt = np.linalg.svd(A)

print("U:",np.round(U, decimals=1))
print("S:",np.round(Vt, decimals=1))
print("Vt:",np.round(S,1))

# A = U S Vt ?

s = np.array([[3.5,0,0],
              [0,3.2,0]])

b = np.dot(np.dot(U,s),Vt)
print("A=",np.round(b,decimals=1))
