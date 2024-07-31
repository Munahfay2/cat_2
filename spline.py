import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


x_data = np.array([3.00, 5.25, 6.25, 8.81, 10.20, 11.60])
y_data = np.array([8.2, 8.1, 5.0, 4.0, 2.5, 7.0])


cs = CubicSpline(x_data, y_data)


x_new = np.linspace(2, 10.6, 100)
y_new = cs(x_new)


plt.scatter(x_data, y_data, label='Data')
plt.plot(x_new, y_new, label='Cubic Spline', color='red')
plt.legend()
plt.show()