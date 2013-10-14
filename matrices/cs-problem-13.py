#
# CS Problem 13
# Author: Daniel Wechsler
#

from numpy import pi,arange,concatenate
from scipy import fft
from pylab import subplot,plot,show
import fastFourierTransformation



N   = pow(2, 8)
L   = 8
dx  = 2.*L/N
x   = (arange(N) - N/2) * dx
k   = 2 * pi / (N*dx) * (arange(N) - N /2)
f   = 1/(1 + x *x)

# Compute fft using scipy implementation
F1  = fft(f)

# Compute fft using own implementation 
F2  = fastFourierTransformation.fastFourierTransformation(f)


f1  = concatenate((F1[N/2 : N], F1[0 : N /2]))
f2  = concatenate((F2[N/2 : N], F2[0 : N /2]))

# Plot the function and the fourier transformations
subplot(312)
plot(x,f)
subplot(311)
plot(k,F1.real, color="blue")
plot(k,F1.imag, color="magenta")

subplot(310)
plot(k,F2.real, color="blue")
plot(k,F2.imag, color="magenta")
show()

