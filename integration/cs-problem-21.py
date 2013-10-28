#
# CS Problem 21
# Author: Daniel Wechsler
#

import numpy as np
from scipy.linalg import solve
from fractions import Fraction

# Computed in previous exercise
coefficients = [1375.0/576.0, 125.0/144.0, 335.0/96.0, 125.0/144.0, 1375.0/576.0]


#
# Basically computes the integral of f for the interval [a,b].
# The implementation was a bit of trial and error process towards
# the correct answer sqr(pi)....
#
def fivepoint (f, a, b, B) :

    # Define equally spaced blocks
    blocks = np.linspace(a, b, B+1)
    integral = 0.0
    for i in range (0, B) :
        subA    = blocks[i]
        subB    = blocks[i+1]
        # Define 7 equally distributed nodes in the block [s0, s1 ... s7]
        stu =  np.linspace(subA, subB, 7)
        s = 0.0
        for k in range (1, 6) : # For s1 to s6 compute f(sx) * coefficient[sx-1] -> we ignore the interval border (open type formula)
            s += f(stu[k]) * coefficients[k-1]

        s = s /B        # Compute integral of block
      
        integral += s   # Sum over blocks
    return integral * (b-a) * 0.1



def exponential (x) :
    return np.exp(-1*pow(x, 2))
     


integral = fivepoint(exponential, -10, 10, 1000)
print ("Integral %f " % integral * 2)




