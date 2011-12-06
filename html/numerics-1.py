import matplotlib.pyplot as plt
from sympy.mpmath import plot, log

fig = plt.figure()
axes = fig.add_subplot(111)
axes.set_title(r"Plot of $f(x)$ in $[0, 0.01]$.")

f = lambda x: x**(1 - log(log(log(log(1/x)))))
plot(f, xlim=[0, 0.01], axes=axes)