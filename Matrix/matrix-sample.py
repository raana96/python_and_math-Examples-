import numpy as np
import sympy as sp

a = np.array([[6,4,24],[1,-9,8]])
print(a) #print a

type(a) #what is a type

a.shape #count of rows and columns

a.size # what is a size

a[0] # The first row of matrix 

a[1] 

a[:,0] 


a[:,2] 

print(a)

a[1][2]

a = np.array([[6,4,24],[1,-9,8],[1,2,3]])
print(a)

a[0:2, :2]

a = np.array([[1,2],[3,4]])
print(a)

a.sum()

a.sum(axis=0)

a.sum(axis=1)

b = a * 2
print(b)

a = np.array([[4,5],[2,0]])
b = np.array([[4,6],[7,1]])
print(a)
print(b)

print(a + b)

print(a - b)

print(a * b)

np.dot(a,b)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[10,11],[20,21],[30,31]])
print(a)
print(b)

a.shape

b.shape

c = np.dot(a,b)
print(c)

d = np.dot(b,a)
print(d)

a = np.array([[1,2,3],[4,5,6]])
a.T

a.T.T

a = np.array([[0,1,2],[1,7,8],[2,8,9]])
print(a)

b = a.T
print(b)

a == b

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

np.trace(a)

b = a.T
b

np.trace(b)

x = np.array([[8,3],[4,2]])
print(x)

np.linalg.det(x)

y = np.array([[1,2,3],[3,1,2],[0,0,1]])
print(y)

np.linalg.det(y)

z = np.array([[5,6,9],[0,4,5],[0,0,2]])
print(z)

np.linalg.det(z)

a = np.array([[4,3],[3,2]])
print(a)

np.linalg.inv(a)

b = np.array([[1,2,3],[0,1,4],[5,6,0]])
print(b)

np.linalg.inv(b)

a = np.array([[1,2],[3,4]])
print(a)

(1**2 + 2**2 + 3 **2 + 4 **2 ) ** (1/2)

np.linalg.norm(a)

np.sqrt(np.trace(a.dot(a.T)))



a = sp.Matrix([[8,3],[4,2]])
a

a.row(0)

a.col(0)

a.shape

a.inv()

a.det()

sp.zeros(4,5)

sp.eye(5)

sp.diag(1,2,3,4)