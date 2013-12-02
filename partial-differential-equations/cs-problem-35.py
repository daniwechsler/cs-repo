#
# CS Problem 35
# Author: Daniel Wechsler
#


import numpy as np
import matplotlib.pyplot as plt
from numpy import exp,arange
import math


#
# The function that is used as initial condition
#
def gauss(x, a, x0):
    return np.exp(-np.power(x - x0, 2.) / 2 * np.power(a, 2.))




#####################################


#
# Approximation of the second derivative of f with respect to x
# using the 2nd order central formula:
#
# dx2 = f(x+dx)+f(x-dx)-2f(x) / dx^2
#
# Idea:  Compute  f(x+dx) and f(x-dx) by shifting  fx to the left and
# right respectively. To conserve the lengths (number of data points)
# of fx, f(x+dx) and  f(x-dx) I extend the starting and/or end points
# of the arrays.
#
def dx2 (fx, dx) :

   # Prepend and append a value to fx.
   fx_ext         = np.append(fx, fx[len(fx)-1])   
   fx_ext         = np.insert(fx_ext, 0, fx[0])

   # Shift fx to right (+dx) by prepending values.
   fx_plus_dx     = np.insert(fx, 0, fx[0])
   fx_plus_dx     = np.insert(fx_plus_dx, 0, fx[0])

   # Shift fx to left (-dx) by appending values.
   fx_minus_dx    = np.append(fx, fx[len(fx)-1])
   fx_minus_dx    = np.append(fx_minus_dx, fx_minus_dx[len(fx_minus_dx)-1])

   # Remove the first and last value of the resulting array such that
   # incoming fx and returned dx2 have same length.
   dx2 = (fx_plus_dx + fx_minus_dx - 2*fx_ext) / (dx*dx)
   dx2 = np.delete(dx2, len(dx2)-1)
   dx2 = np.delete(dx2, 0)
 
   return dx2
   
#
# The Fisher-Kolmogorov equation. Second derivative is approximated with
# the 2nd order central formula.
#
def F(fx, dx) :
   return fx * (1-fx) + dx2(fx, dx)
   
#
# Perform one step by computing fn+0.5 and fn+1 using fn+0.5.
#
def evolve (fn, dt, dx) :

   fn_half = fn + 0.5*dt*F(fn, dx)
   fn_full = fn + dt * F(fn_half, dx)
   return fn_full
   
#####################################


# Initial conditions and parameters
dx    = 0.1                
dt    = 0.001
x     = np.arange(-10,10,dx)  
fx0   = gauss(x, 2.5, 0)         # Using gaussian function as initial condition


fn    = fx0 
for i in range (1001) :          # Evolve for 1000 steps
   
   if i % 50 == 0 :              # Plot current function every 50th step
      if i%200 == 0 :
         label = "Time: %i * $\Delta$t" % i
         plt.plot(x, fn, label=label)
      else :
         plt.plot(x, fn)
         
   fn = evolve(fn, dt, dx)   



plt.legend(loc='upper right', shadow=True, prop=dict(size=10))
plt.title("Fisher-Kolmogorov equation: $\Delta$t=%.3f $\Delta$x=%.3f" % (dt, dx))   
plt.show()






