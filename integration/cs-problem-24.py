#
# CS Problem 24
# Author: Daniel Wechsler
#


import matplotlib.pyplot as plt
import numpy as np
import chebyshev as ch


n = 5
M = 10        
# Compute first n Chebyshev polynomials using gauss Chebyshev quadrature
L = ch.Chebyshev(n, "gauss", M)              
x = np.arange(-1, 1, 0.01)  

# Plot the polynomials
for l in range (0, len(L)) :
    y = []    
    for i in x :
        y.append(ch.evalp(i, L[l]))
    plt.plot(x, y)

plt.show()


