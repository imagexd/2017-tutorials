"""
### Exercise: integrating periodic functions

In a [recent blog post](https://www.johndcook.com/blog/2017/03/01/numerically-integrating-periodic-functions/), John Cook shows that there are functions for which the trapezoid rule for integration does not work very well.

For this one it works great:

$g(x) = \exp(\cos(x))$

But not for:

$h(x) = \exp\left(1-x^2/2\right)$

- Implement both functions, taking care to make the latter periodic
- Use `scipy.integrate.trapz` to find their integrals between $[-\pi, \pi]$
- Create a plot of sample point vs accuracy, as in the end of the blog post

The exact solution for $g$ is:

$2 \pi I_0(1)$

And for $h$:

$e \sqrt{2\pi}\ \mathrm{erf} \left(\frac{\pi \sqrt{2}}{2} \right)$
"""

import numpy as np

import matplotlib.pyplot as plt

from scipy.special import erf, iv  # <-- you'll need these!
from scipy import integrate

def h(x):
    return np.exp(1 - x**2 / 2)

def g(x):
    return np.exp(np.cos(x))

N = np.arange(2, 10)

errors_g = []
errors_h = []
ideal_g = 2 * np.pi * iv(0, 1)  # checked: 7.954926521012845274513219665329394328161342771816638573400
ideal_h = np.e * np.sqrt(2 * np.pi) * erf(np.pi * np.sqrt(2) / 2)  # checked: 6.802272881091337524383192561126225790801223370160697859404

for n in N:
    t = np.linspace(-np.pi, np.pi, n, endpoint=True)

    I = integrate.trapz(g(t), t)
    errors_g.append(np.abs(ideal_g - I))

    I = integrate.trapz(h(t), t)
    errors_h.append(np.abs(ideal_h - I))

plt.semilogy(N, errors_g, label='Error for g')
plt.semilogy(N, errors_h, label='Error for h')
plt.legend()
plt.xlabel('Integration points')
plt.ylabel('Log of absolute error')

plt.show()
