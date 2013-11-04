#
# CS Problem 21
# Author: Daniel Wechsler
#

import numpy as np
from scipy.linalg import solve
from fractions import Fraction
import integration_functions as fp



def exponential (x) :
    return np.exp(-1*pow(x, 2))
     
integral = fp.fivepoint(exponential, -10, 10, 1000)
print ("Integral %f " % integral * 2)




