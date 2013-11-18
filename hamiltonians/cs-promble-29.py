#
# CS-Problem 29:
# Author: Daniel Wechsler
#

from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show


#
# The function defines the Lotka-Volterra System
#
# dx/dt = ax - xy
# dy/dt = xy - y
#
def lotkaVolterra (xy, t, a) :
    x   = xy[0]
    y   = xy[1]
    dx  = a*x - x*y
    dy  = x*y - y
    return [dx, dy]

#
# The hamiltons equation.
#
# dp = -@H/@q
# dq =  @H/@p
#
# With H being the Hamiltonian:
# H(p,q) = epx(p)+exp(q)-p-aq
#
def hamiltonian (pq, t, a) :
    p   = pq[0]
    q   = pq[1]
    dp  = -1 * (exp(q) - a)     # Derivative of H with respect to q
    dq  = exp(p) - 1            # Derivative of H with respect to p
    return [dp, dq] 
    
#
# A transformation function used to accommodate the
# relation p=ln(x), q=ln(x)
#
def mapf (pq) :
    p = pq[0]
    q = pq[1]
    x = exp(p)
    y = exp(q)
    return [x, y]




xy0A        = [2,5]                                 # Initial conditions A
xy0Trans    = [np.log(xy0A[0]), np.log(xy0A[1])]    # Transform initial conditions according to p = ln(x), q=ln(y)
xy0B        = [1,5]                                 # Initial conditions B
xy0BTrans   = [np.log(xy0B[0]), np.log(xy0B[1])]    # 
t           = np.linspace(0, 10, 200)               # The Domain

#
# Integrate Lotka-Volterra system and Hamitonian System (equivalent)
# under different conditions/parameters.
#

figsize = (22,12) 
figure = plt.figure(figsize = figsize)
plt.subplots_adjust(hspace = .3, wspace=0.04, left=0.03)

#
# Parameter a=15
#
a           = 15  # Parameter alpha
XYham       = odeint(hamiltonian, xy0BTrans, t, args=(a,))
XYlv        = odeint(lotkaVolterra, xy0A, t, args=(a,))
XYhamTrans  = map(mapf, XYham) # Transform p, q to x, y

plt.subplot(521)
plt.plot(t, XYlv)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0A[0], xy0A[1], a))

plt.subplot(522)
plt.plot(t, XYhamTrans)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0B[0], xy0B[1], a))


#
# Parameter a=8
#
a           = 8   
XYham       = odeint(hamiltonian, xy0BTrans, t, args=(a,))
XYlv        = odeint(lotkaVolterra, xy0A, t, args=(a,))
XYhamTrans  = map(mapf, XYham) # Transform p, q to x, y

plt.subplot(523)
plt.plot(t, XYlv)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0A[0], xy0A[1], a))

plt.subplot(524)
plt.plot(t, XYhamTrans)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0B[0], xy0B[1], a))


#
# Parameter a=5.5
#
a           = 5.5   
XYham       = odeint(hamiltonian, xy0BTrans, t, args=(a,))
XYlv        = odeint(lotkaVolterra, xy0A, t, args=(a,))
XYhamTrans  = map(mapf, XYham) # Transform p, q to x, y

plt.subplot(525)
plt.plot(t, XYlv)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0A[0], xy0A[1], a))

plt.subplot(526)
plt.plot(t, XYhamTrans)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0B[0], xy0B[1], a))


#
# Parameter a=4
#
a           = 5  
XYham       = odeint(hamiltonian, xy0BTrans, t, args=(a,))
XYlv        = odeint(lotkaVolterra, xy0A, t, args=(a,))
XYhamTrans  = map(mapf, XYham) # Transform p, q to x, y

plt.subplot(527)
plt.plot(t, XYlv)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0A[0], xy0A[1], a))

plt.subplot(528)
plt.plot(t, XYhamTrans)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0B[0], xy0B[1], a))


#
# Parameter a=1
#
a           = 1   
XYham       = odeint(hamiltonian, xy0BTrans, t, args=(a,))
XYlv        = odeint(lotkaVolterra, xy0A, t, args=(a,))
XYhamTrans  = map(mapf, XYham) # Transform p, q to x, y

plt.subplot(529)
plt.plot(t, XYlv, label='line 1')
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0A[0], xy0A[1], a))

plt.subplot(5,2, 10)
plt.plot(t, XYhamTrans)
plt.title("Initial conditions x=%.2f y=%.2f and parameter a=%.2f" % (xy0B[0], xy0B[1], a))

plt.show()

#
# The population equilibriums of the Lotka-Volterra system are at:
# x,y = 0,0
# x,y = 1,a
#
# In the right column of plots we approach a = y (with x=1). Thus an equilibrium
# state of the system (4th plot right column).
#




