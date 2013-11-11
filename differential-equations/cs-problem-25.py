#
# CS Problem 25
# Author: Daniel Wechsler
#


import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import odeint
from numpy import exp


def eulerMethod (y0, x0, xMax, f, h) :

    Xn  = []
    Yn  = []
    xn  = x0
    yn  = y0
    while xn<=xMax :
        Xn.append(xn)
        Yn.append(yn)
        ynext   = yn+h*f(yn, xn)
        xn      += h
        yn      = ynext

    return Yn, Xn


def rungeKuttaMethod (y0, x0, xMax, f, h) :

    Xn  = []
    Yn  = []
    xn  = x0
    yn  = y0
    while xn<=xMax :
        Xn.append(xn)
        Yn.append(yn)
        ynext   = yn+h*f(yn+0.5*f(yn, xn), xn)
        xn      += h
        yn      = ynext

    return Yn, Xn


def rungeKuttaForthOrderMethod (y0, x0, xMax, f, h) :
    
    Xn  = []
    Yn  = []
    xn  = x0
    yn  = y0

    while xn<=xMax :
       
        Xn.append(xn)
        Yn.append(yn)
        f1      = f(yn, xn)
        f2      = f(yn + 0.5*h*f1, xn)
        f3      = f(yn + 0.5*h*f2, xn)
        f4      = f(yn + h*f3, xn)
        ynext   = yn+(1.0/6.0)*h*f((f1 + 2*f2 + 2*f3 + f4), xn)
        xn      += (1.0/6.0)*h
        yn      = ynext

    return Yn, Xn




def f (y, x) :
    return 2*x*y


xMin    = 0.0
xMax    = 2.0
h       = 0.2
y0      = 4.0


YnEuler, XnEuler    = eulerMethod(y0, xMin, xMax, f, h)
YnRK, XnRK          = rungeKuttaMethod(y0, xMin, xMax, f, h)
YnRKfo, XnRKfo      = rungeKuttaForthOrderMethod(y0, xMin, xMax, f, h)
t = np.linspace(xMin, xMax, 60)


plt.title('dy/dx = 2*x')

p1 = plt.plot(XnEuler, YnEuler, label='Euler')
p2 = plt.plot(XnRK, YnRK, label='Runge-Kutta')
p3 = plt.plot(XnRKfo, YnRKfo, label='Fourth-Order-Runge-Kutta')
p4 = plt.plot(t, odeint(f, y0, t), label='Scipy')

legend = plt.legend(loc='upper left', shadow=True)

plt.show()


