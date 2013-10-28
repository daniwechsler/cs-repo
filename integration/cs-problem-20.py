#
# CS Problem 20
# Author: Daniel Wechsler
#


import numpy as np
from scipy.linalg import solve
from fractions import Fraction


# Init matrix A and vector B with 1's
A = np.ones(3*3).reshape(3,3)
B = np.ones(3)

for i in range (0, 3) :

    # Compute B[i]
    k       = i+1 + i     
    B[i]    = 1.0/k * pow(5, k)
    
    for j in range (0, 3) :
        # Compute A[i,j]
        A[i,j] = pow(j*2, i*2)

    
A[0,0]  = 0.5
X       = solve(A, B)


print "Coefficients (rounded):"
print ("c0=%s" % str(Fraction(X[0]).limit_denominator(1000)))
print ("c0=%s" % str(Fraction(X[1]).limit_denominator(1000)))
print ("c0=%s" % str(Fraction(X[2]).limit_denominator(1000)))
    

