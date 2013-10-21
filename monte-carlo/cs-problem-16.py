#
# CS Problem 16
# Author: Daniel Wechsler
#

import math
import random
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

#
# The class is used to simulate a walker. It performs
# N steps in a random direction with a given step size.
#
class Walker :

    stepSize    = 1.0

    x           = 0.0   # Current x position

    y           = 0.0   # Current y position

    #
    # Init random Walker with given step size
    #
    def __init__(self, stepSize):
        self.stepSize = stepSize
        
    #
    # Resets the Walker to initial values
    #
    def reset (self) :
        self.x = 0.0
        self.y = 0.0

    #
    # Lets the walker walk for N steps
    #
    def walk (self, N) :
        n = 0
        while n<N :
            self.step()
            n += 1

    #
    # Do a single step in a random direction with step size = self.stepSize
    #
    def step (self) :
        # Get Random angle
        angle = random.uniform(0, 2*math.pi)
        # Compute distance in x and y
        dx = math.sin(angle) * self.stepSize
        dy = math.sin(math.pi/2 - angle) * self.stepSize
        # Perform step
        self.x += dx
        self.y += dy


    def getDistance (self) :
        return math.sqrt(self.x*self.x + self.y * self.y)

    def getXDistance (self) :
        return 0.0 - self.x

    def getYDistance (self) :
        return 0.0 - self.y



walks           = 10000         # Number of walks to sumulate
N               = 50            # Number of steps
stepLength      = 2.0           # Length of a single step
distances       = []            # Holds all distances computed by the Walker
xDistances      = []
yDistances      = []
walker          = Walker(stepLength)    # Init the random Walker


# Simulate the walks and store results in corresponding lists
n           = 0
maxDist     = 0.0   # Store max dist to compute axis width
maxXDist    = 0.0
while n<walks:      
    walker.reset()
    walker.walk(N)

    distances.append(walker.getDistance())
    xDistances.append(walker.getXDistance())
    yDistances.append(walker.getYDistance())

    if maxDist < walker.getDistance() :
        maxDist = walker.getDistance()

    if maxXDist < walker.getXDistance() :
         maxXDist = walker.getXDistance()
         
    n += 1



# Plot distance distribution
plt.subplot(311)
plt.title('Random Walk (N=%i, step-size=%.2f, number of walks=%i)' % (N, stepLength, walks)) 
n, bins, patches    = plt.hist(distances, 50, normed=True, color='red')
d                   = np.linspace(0,int(maxDist),100)
# Compute distribution according to formula (5.2) with step size parameter introduced
pd                  = 2 * np.array(d) / (N*pow(stepLength,2)) * np.exp(pow(np.array(d),2)*-1 / (N*pow(stepLength,2)))
plt.plot(d, pd)

# Plot x distance distribution
plt.subplot(312)
n, bins, patches    = plt.hist(xDistances, 50, normed=True, color='red')
x                   = np.linspace(-math.fabs(maxXDist),math.fabs(maxXDist),100)
# Compute distribution according to integral of (5.1) for one dimension
px                  = 1.0/(math.sqrt(N*math.pi*pow(stepLength,2))) * np.exp(-1*pow(np.array(x), 2) / (N * pow(stepLength,2)))

plt.plot(x, px)

# Plot y distance distribution
plt.subplot(313)
n, bins, patches    = plt.hist(yDistances, 50, normed=True, color='red')
y                   = np.linspace(-15,15,100)
py                  = 1.0/(math.sqrt(N*math.pi*pow(stepLength,2))) * np.exp(-1*pow(np.array(x), 2) / (N * pow(stepLength,2)))
plt.plot(y, py)


plt.show()













