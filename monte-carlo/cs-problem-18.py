#
# CS Problem 18
# Author: Daniel Wechsler
#

import math
import matplotlib.pyplot as plt
from pylab import subplot,plot,show
import matplotlib
import random
import numpy as np


#
# Simulates the puppet. Given N1 and N2 it randomly moves a step
# (length depending on N1/N2) either forward or backward.
# The field self.maxDist holds the maximum distance the puppet has
# moved away from the origin
#
class Puppet :

    N1Init          = 0

    N2Init          = 0
    
    N1              = 0

    N2              = 0

    stepN1          = -1.0

    stepN2          = 1.0

    dist            = 0

    maxDist         = 0.0

    def __init__(self, N1, N2):
        self.N1             = N1
        self.N2             = N2
        self.N1Init         = N1
        self.N2Init         = N2
        # Compute step size such that we end at origin
        r = float(N1) / float(N2)
        self.stepN2 = self.stepN1 * r * -1
        
                   
    def forward (self) :
        self.dist += self.stepN1
        self.updateMaxDist()

    def backward (self) :
        self.dist += self.stepN2
        self.updateMaxDist()

    def updateMaxDist (self) :
        if math.fabs(self.dist) > self.maxDist :
            self.maxDist = math.fabs(self.dist)

    def start (self) :
        while self.N1 > 0 and self.N2 > 0 :
            self.step()
        
    def step (self) :
        rand = random.randint(0, 1)
        if (rand == 0) :
            if self.N1 > 0 :
                self.N1 -= 1
                self.forward()
        else :
            if self.N2 > 0 :
                self.N2 -= 1
                self.backward()

    # Return normalized max distance
    def getMaxDist (self) :
        return self.maxDist / (self.N1Init+self.N2Init) 

    
N1  = 24
N2  = 36
i   = 0
# Simpulate 1000 walks
distances = []
while i<400 :
    puppet = Puppet(N1, N2)
    puppet.start()
    
    distances.append(puppet.getMaxDist())   # Store max distance
    i += 1


x = np.arange(0, 1, 0.01)
n, bins, patches    = plt.hist(distances, cumulative=True, bins=50, normed=True)

# Calculate KS statistics distribution for given N1 and N2
v   = math.sqrt(N1*N2/(N1+N2))
u   = v + 0.12 + 0.11/v
x   = np.linspace(0.0, 1.0, 101)
k   = 0
r   = None
while k<1000 : # Compute (5.11) for a range of k. A bit circuitous - I konw
    y   = 2 * (pow(-1, k) * np.exp(-2 * pow((k+1),2) * pow(u,2) * pow(np.array(x), 2))) 
    if r == None :
        r = y
    else :
        r   = np.add(r, y)
    k   += 1


# Well something is wrong here. The histogram is shifted to the right - Don't
# know maybe the method computing the maxDistance (normalized) is wrong. 
plt.plot(x, 1-r)
plt.show()






