#
# CS Problem 23
# Author: Daniel Wechsler
#


import matplotlib.pyplot as plt
import numpy as np
import chebyshev as ch


n = 5
B = 1000        # Hight B is required
# Compute first n Chebyshev polynomials using newton algorithm
L = ch.Chebyshev(n, "newton", B)              
x = np.arange(-1, 1, 0.01)  

# Plot the polynoms
for l in range (0, len(L)) :
    y = []    
    for i in x :
        y.append(ch.evalp(i, L[l]))
    plt.plot(x, y)

plt.show()


