#
# CS Problem 39
# Author: Daniel Wechsler
#


from scipy import fft, ifft
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp,arange
import random
import copy
import math
from matplotlib import animation




#######################################
# Potential Functions                 #
#######################################
   
#
# Given an  array of  x values  the function returns a
# double well potential over the  x value according to
# V(x) = 0.5*|x-1|^2
#
def doubleWellPotential (x) :
   ab = abs(x-1)
   y = ab*ab*0.5
   return y


#
# Returns  a potential that  represents a  barrier  of
# width 2 and height 2 at the specified position on x.
#
def barrierPotential (x, position) :
    y = copy.copy(x)
    index = 0
    for i in x :
      if i > position-1 and i < position+1 :
         y[index] = 2
      else :
         y[index] = 0
      index += 1
    return y


#######################################
# Schroedinger                        #
#######################################

#
# Implementations the evolution of the 1D Schroedinger
# equation.
#
class Schroedinger :
    
    #
    # Int: Defines the number of steps computed for one call of
    # the evolve() method.
    #
    S        = 10
    
    #
    # Float: Time change for one step
    #
    dt       = 0.01

    #
    # Array: Values of x domain
    #
    x        = None

    #
    # Array: Values of k domain
    #
    k        = None

    #
    # Array: Describing the initial wave function for x.
    #
    x0       = None

    #
    # Array: The current values of the wave function in spacial dimension.
    #
    xCurrent = None

    #
    # Array: The current values of the momentum wave function.
    #
    kCurrent = None
    
    #
    # Array: The values of the potential V.
    #
    xV       = None

 
    #
    # x   := Array defining N points on x
    # x0  := Array representing the initial wave function for x
    # Vx  := Array being the potential over x
    # k   := Array defining N points on k
    #
    def __init__(self, x, x0, xV, k, dx, dk, S) :

        self.x          = x
        self.k          = k
        self.xCurrent   = x0
        self.xV         = xV
        self.dx         = dx 
        self.dk         = dk
        self.S          = S
        self.fft()      # Compute initial k values
 
    #
    # Performs self.S steps according to the following procedure:
    # 1) Perform half step in x direction.
    # 2) Compute Fourier Transformation (k) of current x.
    # 3) Perform full step in k direction.
    # 4) Compute inverse Fouriere Transformation of k.
    # 5) Compute another half step for x.
    #
    def evolve (self) :

        for a in range (self.S) :          
            self.halfStepX()
            self.fft()
            self.fullStepK()
            self.inverseFft()
            self.halfStepX()
            self.fft()  
 

    #
    # Computes half step for x.
    #
    def halfStepX (self) :
        self.xCurrent = self.xCurrent * np.exp(-1/2 * self.xV * self.dt * 1j)

    #
    # Computes full step for k.
    # 
    def fullStepK (self) :
        self.kCurrent = self.kCurrent*np.exp(-1/2*1j*(self.k*self.k)*self.dt)

    #
    # Compute k by Fourier Transformation of x.
    #
    def fft (self) :
        # Transform x before FFT (shift and shrink)
        tempX = self.xCurrent * np.exp(-1j * self.k[0] * self.x) * self.dx / np.sqrt(2 * np.pi)
        tempK = fft(tempX)
        self.kCurrent = tempK

    #
    # Compute x by inverse fourier transformation of k
    #
    def inverseFft (self) :
        tempX = ifft(self.kCurrent)
        # Transform x after inverse FFT (shift and stretch)
        self.xCurrent = tempX / np.exp(-1j * self.k[0] * self.x) / self.dx * np.sqrt(2 * np.pi)


def initialWaveFunction(x, a, x0, k0):
    return ((a * np.sqrt(np.pi)) ** (-0.5)* np.exp(-0.5 * ((x - x0) * 1. / a) ** 2 + 1j * x * k0))

   
#
# Initial Conditions
# Depending on the choosen potential function we
# have to use slightly different initial conditions.
#


N     = 2**12                               # Number of points on x
dx    = 0.05                                # Distance between points on x
k0    = 1                                   # Initial momentum average   
x0    = -20                                 # Initial position average
dk    = 2 * np.pi / (N * dx)                # Distance between points on k
x     = dx * (np.arange(N) - 0.5 * N) 
k     = -40 + dk * np.arange(N)
xInit = initialWaveFunction(x, 6, x0, 1)    # Get initial wave function (gaussian)

POTENTIAL_FUNCTION = "DOUBLE_WAVE";         # Use not "DOUBLE_WAVE" for barrier potential

if POTENTIAL_FUNCTION == "DOUBLE_WAVE" :
    
    xV      = doubleWellPotential(x)
    S       = 10
    # Plotting parameters
    kXLimit     = 40
    interval    = 200
      
else :
   
    xV = barrierPotential(x, 20)
    S     = 80
     
    # Plotting parameters
    kXLimit     = 4
    interval    = 1
    


# Create instance of Schroedinger that computes evolution of particle in 1D
S = Schroedinger(x, xInit, xV, k, dx, dk, S)



#######################################
# Plotting                            #
#######################################

fig         = plt.figure()
# x
xAxis       = fig.add_subplot(211, xlim=(-100, 100), ylim=(-0.5, 1.5))
xAxis.set_xlabel("x")
xAxis.set_ylabel("|w(x,t)|")
xLine,      = xAxis.plot([], [], label="position (prob dist)")      # Position on x
vLine,      = xAxis.plot([], [], label="potential V(x)")            # The potential
legend      = plt.legend(loc='upper right', shadow=True, prop=dict(size=10))

# k
kAxis       = fig.add_subplot(212, xlim=(-kXLimit, kXLimit), ylim=(-0.5, 2.5))
kLine,      = kAxis.plot([], [], label="momentum (prob dist)")      # Momentum
legend      = plt.legend(loc='upper right', shadow=True, prop=dict(size=10))
kAxis.set_xlabel("k")
kAxis.set_ylabel("|w(k,t)|")


def init():
    xLine.set_data([], [])
    kLine.set_data([], [])
    vLine.set_data([], [])
    return xLine, kLine, vLine

#
# Update function that is called periodically by the animation.
#
def animate(i):
    
   # Evolve Schroedinger equation for some steps
   S.evolve()
   
   x    = S.x
   k    = S.k
   y    = abs(S.xCurrent)
   y2   = abs(S.kCurrent)
   xLine.set_data(x, 4*y)
   kLine.set_data(k, y2)

   vLine.set_data(x, S.xV)
   return xLine, kLine, vLine

# Start animation
anim = animation.FuncAnimation(fig, animate, init_func=init,
           frames=200, interval=interval, blit=True)

plt.show()


   
