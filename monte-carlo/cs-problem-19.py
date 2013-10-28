#
# CS Problem 19
# Author: Daniel Wechsler
#

import math
import matplotlib.pyplot as plt
import matplotlib
import random
import numpy as np
from pylab import subplot,plot,show


#
# Simulates the light house. 
#
class Lighthouse :

    phiMax  = 0.0

    phiMin  = 0.0

    a       = 0.0

    b       = 0.0

    def __init__(self, a, b):
        self.a          = a
        self.b          = b
        # Max phi since x is limited to [-1,1]
        self.phiMax     = math.atan((1-a)/b)        
        self.phiMin     = math.atan((-1-a)/b)

                   
    def flash (self) :
        
        phi = random.uniform(self.phiMin, self.phiMax)
        x   = self.a + self.b * math.tan(phi)
        return x

    #
    # Performs N flashes and returns the corresponding
    # x values,
    #
    def run (self, N) :
        X   = []
        n = 0
        while n<N :
            x = lighthouse.flash()
            X.append(x)
            n += 1
        return X            


#
# Implementation of the metropolitan algorithm
#
class Metropolitan :

    MAX_STEP_SIZE   = 0.12

    MIN_STEPS       = 50
    
    a               = 0.0

    b               = 0.0

    def __init__(self) :
        # Compute initial a and b (just random value within allowed range)
        self.a = random.uniform(-1.0, 1.0)
        self.b = random.uniform(0.0001, 1.0)

    #
    # Used to generate the next a,b position randomly
    #
    def step (self, k, low, up) :
        # Computes a step such that k + step > low and < up
        while True:
            dk = random.uniform(-self.MAX_STEP_SIZE, self.MAX_STEP_SIZE)
            if k+dk <= up and k+dk > low :
                return dk

    #
    # Computes the joint probability given a distribution X, a and b.
    #
    def jointProbability (self, X, a, b) :
        p = b/((pow(a,2) - 2*a*np.array(X) + pow(b,2) + pow(np.array(X),2))*(math.atan((1.-a)/b) + math.atan((1.+a)/b)))
        return np.prod(p)


    def run (self, X) :

        jp  = self.jointProbability(X, self.a, self.b)

        step = 0
        while True:

            da      = self.step(self.a, -1.0, 1.0)
            db      = self.step(self.b, 0.0, 1.0)
            jpNext  = self.jointProbability(X, self.a+da, self.b+db)

            if jp == 0 or random.uniform(0, 1) < jpNext / jp :
                self.a += da
                self.b += db
                jp = jpNext
              
            if jp == 0 :
                continue

            step += 1 
            if step > self.MIN_STEPS and jpNext/jp >= 1.0:
                return (self.a, self.b)
        


aReal       = -0.5          # The a we want to infer
bReal       = 0.2           # The b we want to infer
N           = 200           # Number of x values to be generated


lighthouse  = Lighthouse(aReal, bReal)
X           = lighthouse.run(N)         # Generate a distribution of x values
        
NUM_WALKS   = 400   # Number of times we run metropolitan algorithm
A           = []    # Holds all a values generated using the metropolitan algorithm
B           = []    # Holds the corresponding b values
n           = 0

while True:
    metr = Metropolitan()
    a, b = metr.run(X)
    A.append(a)
    B.append(b)
    if n > NUM_WALKS :
        break
    n += 1


plt.subplots_adjust(hspace=0.4)
subX = plt.subplot(311)
plt.xlim([-1,1])
plt.hist(X, bins=50, normed=True, histtype='step')
subX.set_title("X Values")

subA = plt.subplot(312)
plt.xlim([-1,1])
plt.hist(A, bins=50, normed=True, histtype='step')
subA.set_title("Infered probability distribution of a=%.2f" % aReal)

subB = plt.subplot(313)
plt.xlim([0,1])
plt.hist(B, bins=50, normed=True, histtype='step')
subB.set_title("Infered probability distribution of b=%.2f" % bReal)



plt.show()

