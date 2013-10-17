#
# CS Problem 15
# Author: Daniel Wechsler
#

import matplotlib.pyplot as plt
from pylab import subplot,plot,show
import matplotlib
import random


#
# Given an integer base 10 >= 0 the function returns
# a string representation of the number in the given
# base (base > 1 && <= 10).
#
def convertToBase (n, base) :

    digits = []

    while True :
        remainder   = n % base
        n           = n / base
        digits.append(str(remainder))
        if n == 0 : break

    digits.reverse()
    return ''.join(digits)


#
# Returns the Halton sequence from 1 to N using
# the given base.
#
def computeHaltonSequence (N, base) :

    halton = []
    for n in range (1, N+1) :
        # Get string representation in other base
        baseConvert = convertToBase(n, base)
        # Reverse the representation
        reverse = baseConvert[::-1]

        # Compute base 10 representation (to right side of radix point)
        sum = .0
        for i in range (0, len(reverse)) :
            v = float(reverse[i]) *  pow(base, (i*-1)-1)      
            sum += v

        halton.append(sum)

    return halton



# Number of "random" points to compute
N = 1500


haltonSeqBaseTwo    = computeHaltonSequence (N, 2)
haltonSeqBaseThree  = computeHaltonSequence (N, 3)

# Generate plot using python random function insted
randomX = []
randomY = [] 
for i in range (0, N) :
    randomX.append(random.random())
    randomY.append(random.random())


# Plot the halton points and random points (using python random function)
matplotlib.rcParams['axes.unicode_minus'] = False
subplot(2, 1, 1)
plot(haltonSeqBaseTwo, haltonSeqBaseThree, '.')
subplot(2, 1, 2)
plot(randomX, randomY, '.')
show()

# Observation:
# The distribution of dots using the halton method is uniform
# wheras the random dots distribution is more clustered.
#

