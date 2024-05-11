import sympy as sy

x,y = sy.symbols('x,y')

eq1 = sy.Eq((2*x-3*y),7) #2x+3y = 7
eq2 = sy.Eq((3*x-4*y),9) #3x+4y = 9

c = sy.solve((eq1 , eq2), (x,y))

print(c)
