#
# CS-Problem: 31
# Author: Daniel Wechsler
#

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp,arange
import math


#
# Equation 8.22 (relativistic)
#
def relativistic (P, t, w, alpha) :
    x   = P[0]
    y   = P[1]
    px  = P[2] 
    py  = P[3]

    k       = 1+pow((px+y), 2) + pow((py-x), 2)
    dpx     = 1/(2*math.sqrt(k)) - (2*px+2*y)
    dpy     = 1/(2*math.sqrt(k)) - (2*py-2*x)
    dx      = 1/(2*math.sqrt(k)) - (-2*py+2*x)
    dy      = 1/(2*math.sqrt(k)) - (2*y+2*px) - alpha * math.cos(w * t)
    return [dpx, dpy, -dx, -dy]

#
# Equation 8.34 (non-relativistic)
#
def nonRelativistic (P, t, w, alpha) :
    x   = P[0]
    y   = P[1]
    px  = P[2] 
    py  = P[3]
    dpx = px + y
    dpy = py - x
    dx  = x - py
    dy  = y - math.cos(w*t) +px

    return [dpx, dpy, -dx, -dy]

    
alpha       = 0.1
i           = [1, 2, 0, 0]
t           = np.linspace(0, 50, 1000)

figure = plt.figure(figsize = (10, 12))
plt.subplots_adjust(hspace = .4)

# Plot some trajectories for non-relativistic system
plt.subplot(3,2, 1)
plt.title("Non-relativistic (w=0.1)")
PQnrel  = odeint(nonRelativistic, i, t, args=(0.1, alpha))
plt.plot(PQnrel[:,0], PQnrel[:,1])

plt.subplot(3,2, 3)
plt.title("Non-relativistic (w=1)")
PQnrel  = odeint(nonRelativistic, i, t, args=(1, alpha))
plt.plot(PQnrel[:,0], PQnrel[:,1])

plt.subplot(3,2, 5)
plt.title("Non-relativistic (w=2)")
PQnrel  = odeint(nonRelativistic, i, t, args=(2, alpha))
plt.plot(PQnrel[:,0], PQnrel[:,1])

# Plot some trajectories for relativistic system
plt.subplot(3,2, 2)
plt.title("Relativistic (w=0.1)")
PQnrel  = odeint(relativistic, i, t, args=(0.1, alpha))
plt.plot(PQnrel[:,0], PQnrel[:,1])

plt.subplot(3,2, 4)
plt.title("Relativistic (w=1)")
PQnrel  = odeint(relativistic, i, t, args=(1, alpha))
plt.plot(PQnrel[:,0], PQnrel[:,1])

plt.subplot(3,2, 6)
plt.title("Relativistic (w=2)")
PQnrel  = odeint(relativistic, i, t, args=(2, alpha))
plt.plot(PQnrel[:,0], PQnrel[:,1])

plt.show();


