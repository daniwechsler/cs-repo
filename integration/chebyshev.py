#
# Author: Daniel Wechsler
#



import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate
from scipy.linalg import solve
from fractions import Fraction
import integration_functions as fp




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
# Evaluates a polynome defined by c at x and divides the
# resutl by sqrt(1-x^2).
#
def evalChebyp (x, c) :
    n = len(c)-1
    s = c[-1]
    for k in range(n, 0, -1):
        s = x * s + c[k-1]

    s = s / math.sqrt(1.0 - x**2)
    return s


def evalChebypSqr (x, c) :
    cp = evalpSqr(x,c)
    return cp / math.sqrt(1.0 - x**2)


#
# Computes the first n+1 Chebysehv polynomials using the Gram-Schmidt
# orthonormalization process. The function returns a list of those
# polynomials. A polynomial is represented by a list of coefficients:
# [c0*1 + c1*x + c2*x^2 + cn*x^n]
# Depending on the parameter alg = ["newton"|"gauss"] different integration
# procedures are used.
#
def Chebyshev (n, alg = "newton", B=5000) :

    L           = []    # Holds all the computed Legendre polynomials
    nCurrent    = 0
    pCurrent    = [1]   # Holds the current polynomial (initialized with P0(x) = 1
    L.append(pCurrent)
    N           = []    # Holds the normalized polynomials
    
    while nCurrent <= n-1:
     
        
        # Normalize current polynomial
        if alg == "newton" :
            integral            = fp.fivepoint(evalChebypSqr, -1.0, 1.0, B, [pCurrent]);
        elif alg == "gauss" :
            integral            = fp.chebyshevGauss(evalpSqr, B, [pCurrent])
        else :
            return False
    
        length                  = math.sqrt(integral)
        pCurrentNormalized      = map (lambda x : x/length, pCurrent)   
        N.append(pCurrentNormalized)

        # 
        # Pn+1(x) = x^n+1 - (<Pn'(x),x^n+1> * Pn'(x) + <Pn-1'(x),x^n+1> * Pn-1'(x) + ... + <P0'(x), x^n-1> * P0'(x))
        #                    [--------s------------]   [--------s----------------]         [--------s-------------]
        #                    [-------------------------------------- S -------------------------------------------]
        # 
        S   = [0] * (nCurrent+1) # Holds the coefficients of the polynomial  resulting by the computation of 'S'
        for i in range(0, len(N)):

            pProd           = ([0] * (nCurrent+1)) + N[i]               # Pn-i' * x^n-1 (Insert n+1 0's at beginning of coefficient list)
           
            if alg == "newton" :

                dotProduct      = fp.fivepoint(evalChebyp, -1.0, 1.0, B, [pProd])    # Compute dot product  
            elif alg == "gauss" :
                dotProduct      = fp.chebyshevGauss(evalp, B, [pProd])    # Compute dot product
                
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

        # Store found Chebyshev polynomial  Pn+1(X) 
        L.append(pNextN)
        pCurrent    = pNextN
        nCurrent    += 1
        
        continue
      
    return L






