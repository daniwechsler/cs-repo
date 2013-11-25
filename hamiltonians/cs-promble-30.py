#
# CS-Problem: 30
# Author: Daniel Wechsler
#

# Unfortunately I couldn't work on the exercises during the weekend (as
# originally expected) - thus my results are a bit rudimentary...
#

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp,arange
import math
import random as ran


def hamiltonian (q1, q2, p1, p2, w, eps) :
    p, q =1  

#
# Leapfrog evolution of chaotic pendulum
#
def leapfrog (q1, q2, p1, p2, dt, w, eps) :
    q1,q2 = (q1+p1*dt/2, q2 + w * dt/2)
    s1,s2 = (math.sin(q1), eps*math.sin(q1-q2))
    p1,p2 = (p1-(s1+s2)*dt, p2+s2*dt)
    q1,q2 = (q1+p1*dt/2, q2 + w*dt/2)
    return q1,q2,p1,p2

#
# Chaotic pendulum (hamilton)
#
def chaoticPendulum (pq, t, w, eps) : 
    p   = pq[0]
    q   = pq[1]
    dq  = p
    dp  = -math.sin(q) - eps * math.sin(q - w*t)
    return [dp, dq]



eps     = 0.3
w       = -2


# Integrate with odeint
# Produces a plot like the one shown in plots/cs-30-odeint.png

step     = 0
q0       = 0
t        = np.linspace(math.pi, 7*math.pi, 7)
PQ       = odeint(chaoticPendulum, [0, 0], t, args=(w, eps))
while True :

    p0 = ran.uniform(-1.1, 1.1) # Get random p0
      
    PQcurrent       = odeint(chaoticPendulum, [p0, q0], t, args=(w, eps))
    PQ              = np.concatenate((PQ, PQcurrent), 0)
        
    step += 1
    if step > 2000 :
        break


plt.plot(PQ[:,1], PQ[:,0], ',')
plt.show();



n       = 0
dt      = 0.1
Q1      = list()
P1      = list()

t= np.linspace(0, 2*math.pi, 600)
q1 = 0
q2 = 0
p1 = 0
p2 = 0

#
# Generates a plot such as cs-30-odeint_2.png and cs-30-odeint_2-zoom.png
#
while n < 1000 :

    if n%20 :
        q1 = 0
        q2 = 0
        p1 = ran.uniform(-1, 1)
        p2 = ran.uniform(-1, 1)
      
    for time in t :
             
        q1,q2,p1,p2 = leapfrog (q1,q2,p1,p2,dt,w,eps)
        
        if time % math.pi < 0.08:
            Q1.append(q1)
            P1.append(p1)

        
    n += 1


plt.plot(Q1, P1, ',')
plt.show();

# It was not really possible to reproduce the surface of section plot
# as shown in the lecture notes. For both methods (leapfrog/odeint)
# it seems that after some time steps the system some how "breaks out"
# and produces wrong results.






