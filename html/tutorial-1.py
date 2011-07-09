import matplotlib.pyplot as plt
from sympy.mpmath import cplot

fig = plt.figure()
axes = fig.add_subplot(111)
axes.set_title("Density plot of $x^3 - 1$ in the complex plane.")

cplot(lambda x: x**3 - 1, re=[-2, 2], im=[-2, 2], axes=axes)