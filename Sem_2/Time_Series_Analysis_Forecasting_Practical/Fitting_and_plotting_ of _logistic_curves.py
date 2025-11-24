import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def logistic(x, L, k, x0):
    return L / (1 + np.exp(-k*(x-x0)))

x = np.linspace(0, 10, 20)
y = 10 / (1 + np.exp(-0.8*(x-5))) + np.random.normal(0, 0.5, 20)  # noisy data

popt, pcov = curve_fit(logistic, x, y, p0=[10, 1, 5])

x_fit = np.linspace(0, 10, 100)
y_fit = logistic(x_fit, *popt)

plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, label='Fitted Logistic Curve')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()