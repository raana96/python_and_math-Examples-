from scipy.optimize import minimize

# f(x,y) = x^3 + y^3
#g1(x,y)=x^2-1 >= 0
#g2(x,y)=y^2-1 >= 0

def f(A):
    x , y = A
    return x**3 + y**3

def g1(x):
    return x**2-1

def g2(y):
    return y**2-1


cons = ({ 'type': 'eq' , 'fun':g1} , { 'type': 'eq' , 'fun':g2})

res = minimize(f , [1,1], constraints= cons)

print(res.x)
print(res.fun)
