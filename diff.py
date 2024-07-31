import sympy as sp
x = sp.symbols('x')
f = x**4 - x - 4
df = sp.diff(f, x)
print(df)