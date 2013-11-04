import numpy as np
import math

#
# Computes the integral of the function f between a and b.
# f     := Function to be integrated
# a     := Left interval boundary
# b     := Right interval boundary
# B     := Number of blocks 
# args  := Can be a list of additional arguments to f.
#
def fivepoint (f, a, b, B, args = []) :

    coefficients = [1375.0/576.0, 125.0/144.0, 335.0/96.0, 125.0/144.0, 1375.0/576.0]
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
            arguments = []
            arguments.append(stu[k])
            arguments += args
            s += f(*arguments) * coefficients[k-1]

        s = s /B        # Compute integral of block
      
        integral += s   # Sum over blocks
    return integral * (b-a) * 0.1


#
# Computes the integral of f for the interval [-1, 1]
# f     := Function to be integrated
# M     := Number of interpolation points
# args  := Can be a list of additional arguments to f.
#
def chebyshevGauss (f, M, args = []) :

    S = 0.0
    for k in range (0, M-1):
        cosValue = math.cos((float(k)+0.5)*math.pi/float(M-1))
        arguments = []
        arguments.append(cosValue)
        arguments += args
        S += f(*arguments)

    I = S * (math.pi/(M))
    return I




