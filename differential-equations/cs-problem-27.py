#
# CS Problem 27
# Author: Daniel Wechsler
#

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import math

#
# Friedman equation:
# V         := [t,r]
# a         := scale factor
# Omegak    := Parameter
#
def friedman (V, a, Omegak) :
    
    OmegaD  = 0.692         # Cosmological Constant (According to Planck results released in 2013)
    H0      = 0.07200       # Hubble Constant
    Ha      = H0 * math.sqrt(Omegak/math.pow(a,3) + OmegaD)
    dt      = -1/(a*Ha)
    dr      = -1/(math.pow(a,2)*Ha)
    
    return [dt, dr]


OmegakO     = 0.27      # Absolutely not sure about that:
OmegakC     = 1.1       # As far as I understood this parameter determines
                        # the underlying geometry of the universe.
                        # if < 1 open universe 
                        # if > 1 closed universe (sphere)
                        
v0          = [0, 0]    # Initial conditions
a           = np.linspace(1, 0.2, 100)
# Integrate the friedman eq. on [0.2,1.0]
xO          = odeint (friedman, v0, a, args=(OmegakO,))
xC          = odeint (friedman, v0, a, args=(OmegakC,))
RO          = []
TO          = []
RC          = []
TC          = []
for i in range(len(xO)) :
    TO.append(xO[i][0])
    RO.append(xO[i][1])
    TC.append(xC[i][0])
    RC.append(xC[i][1])
    
       

plt.subplot(2, 1, 1)
plt.plot(a, RO)
plt.plot(a, RC)
plt.xlabel('scale factor', fontsize=12)
plt.ylabel('luminosity dist. (Gly)', fontsize=12)

plt.subplot(2, 1, 2)
plt.plot(a, TO)
plt.plot(a, TC)
plt.xlabel('scale factor', fontsize=12)
plt.ylabel('lookback time. (Gyr)', fontsize=12)

plt.show()
