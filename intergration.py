from scipy.integrate import quad

def integrand(x):
    return x**5 - x - 4

result, error = quad(integrand, 1, 3)
print(result)