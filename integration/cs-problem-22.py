#
# CS Problem 22
# Author: Daniel Wechsler
#


import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate
from scipy.linalg import solve
from fractions import Fraction
from pylab import subplot,plot,show
import fivepoint as fp



#
# Evaluates a polynome defined by its coefficients c
# at point x
#
def evalp (x, c) :
    n = len(c)-1
    sum = c[-1]
    for k in range(n, 0, -1):
        sum = x * sum + c[k-1]
    return sum

#
# Evaluates a polynome defined by its coefficients c
# at point x and returns x^2
#
def evalpSqr (x, c) :
    n = len(c)-1
    sum = c[-1]
    for k in range(n, 0, -1):
        sum = x * sum + c[k-1]
    return pow(sum, 2)


#
# Compute square root of integral form P^2 from -1 to 1.
# Where P is defined by the coefficients c
#
def normalizeP (c) :
    integral    = fp.fivepoint(evalpSqr, -1, 1, 10, [c])
    length      = math.sqrt(integral)
    pNormalized = map (lambda x : x/length, c)
    return pNormalized


#
# Computes the first n+1 Legendre polynomials using the Gram-Schmidt
# orthonormalization process. The function returns a list of those
# polynomials (represented as lists of their coefficients)
#
def Legendre (n) :

    L           = []    # Holds all the computed Legendre polynomials
    nCurrent    = 0
    pCurrent    = [1]   # Holds the current polynomial (initialized with P0(x) = 1
    L.append(pCurrent)
    N           = []    # Holds the normalized polynomials
    
    while nCurrent <= n:

        
        # Normalize current polynomial
        pCurrentNormalized = normalizeP(pCurrent)
        N.append(pCurrentNormalized)

        # 
        # Pn+1(x) = x^n+1 - (<Pn'(x),x^n+1> * Pn'(x) + <Pn-1'(x),x^n+1> * Pn-1'(x) + ... + <P0'(x), x^n-1> * P0'(x))
        #                    [--------s------------]   [--------s----------------]         [--------s-------------]
        #                    [-------------------------------------- S -------------------------------------------]
        # 
        S   = [0] * (nCurrent+1) # Holds the coefficients of the polynomial  resulting by the computation of 'S'
        for i in range(0, len(N)):

            pProd           = ([0] * (nCurrent+1)) + N[i]               # Pn-i' * x^n-1 (Insert n+1 0's at beginning of coefficient list)
            dotProduct      = fp.fivepoint(evalp, -1, 1, 10, [pProd])   # Compute dot product  
            s               = map (lambda x : x*dotProduct, N[i])
            
            # Add coefficient of 's' to coefficients of 'S'
            for h in range(0, len(s)) :
                S[h] += s[h]

        
        # Next polynomial  is Pn+1(x) = x^n+1 - S 
        pNext = map(lambda x: x*-1, S)
        pNext.append(1)
    
        # Find parameter 'a' such that Pn+1(1) = 1 and multiply pNext with it.
        xAtOne  = evalp(1.0, pNext)
        a       = 1/xAtOne
        pNextN  = map (lambda x : x*a, pNext)

        # Store found Legendre polynomial  Pn+1(X) 
        L.append(pNextN)
        pCurrent    = pNextN
        nCurrent    += 1
        
        continue
      
    return L

    

n = 4
L = Legendre(n)                 # Compute n+1 Legendre polynomial s            
x = np.arange(-1, 1, 0.01)  

# Plot the polynoms
for l in range (0, len(L)) :
    y = []    
    for i in x :
        y.append(evalp(i, L[l]))
    plot(x, y)

plt.show()


