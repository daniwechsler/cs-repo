#
# CS-Problem: 33
# Author: Daniel Wechsler
#

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp,arange
import math


#
# Evolution according to equation 8.53
#
def blackhole (X, t) :
    x   = X[0]
    y   = X[1]
    px  = X[2]
    py  = X[3]

    r   = math.sqrt(math.pow(x,2) + math.pow(y,2))
    # Derivatives with respect to px, py, x, y 
    dpx = px-(2*x*(py*y+px*x)/math.pow(r,3))
    dpy = py-(2*y*(py*y+px*x)/math.pow(r,3))
    dx  = -2*px*(py*y+px*x)/math.pow(r,3)
    dy  = -2*py*(py*y+px*x)/math.pow(r,3)

    return [dpx,dpy,-dx,-dy]
   
t = np.linspace(0, 5000, 1000)

# Plot some trajectories from different initial conditions

i   = [20,0,0,0.2]
PQ  = odeint(blackhole, i, t)
plt.plot(PQ[:,0], PQ[:,1], label="[x,y,px,py] = [20,0,0,0.2]")


i   = [25,0,0,0.2]
PQ  = odeint(blackhole, i, t)
plt.plot(PQ[:,0], PQ[:,1], label="[x,y,px,py] = [25,0,0,0.2]")

i   = [30,0,0,0.2]
PQ  = odeint(blackhole, i, t)
plt.plot(PQ[:,0], PQ[:,1], label="[x,y,px,py] = [30,0,0,0.2]")


i   = [35,0,0,0.2]
PQ  = odeint(blackhole, i, t)
plt.plot(PQ[:,0], PQ[:,1], label="[x,y,px,py] = [35,0,0,0.2]")
legend = plt.legend(loc='upper left', shadow=True)
plt.show();

