#
# CS Problem 5
# Author: Daniel Wechsler
#

import numpy as np
import matplotlib.pyplot as plt
import math

#
# The function finds all primes below 'n' using the  sieve of Eratosthenes
# method. It returns a list containing all primes <= n.
#
# Idea:
# 1)    Init list of integers [2...n]
#
# 2)    Select current element (At start point its the first
#       element - later the next one to the right of the
#       previously selected element. If there is no such
#       element any more we are done and there are only primes
#       in our list.
#
# 3)    Remove all multiples of the selected element from the list.
#
# 4)    Continue with step 2)
#
# Notes:
# -     List holding none primes is actually not needed in this
#       implementation.
#
def findPrimeNumbers (n):

    
    try:

        if n < 2:
            return []

        # Initialize list that will hold all primes in [2,...n].
        # At init time it holds all natural numbers in the interval.
        primes          = range(2, n+1)
          
        # Initialize list holding none primes
        nonePrimes      = []

        currentIndex    = 0   

        while True:
            
            number                  = primes[currentIndex]
            
            index = currentIndex + 1
            while True:
                   
                length = len(primes)
                if index == length: 
                    break
                
                if primes[index] % number == 0: # The current number in the list is multiple of prime -> put it on none prime list
                    nonePrimes.append(primes.pop(index))
                else:
                    index = index+1 # Current number is not a multiple. Keep it on prime list
               
                            
            currentIndex = currentIndex + 1
            if len(primes)-1 == currentIndex:
                break

        return primes            
         
    except TypeError: # Return empty list if given parameter n is not valid
        return []
    
    
n =  10000
primes = findPrimeNumbers(n)

print ("Primes smaller or equal to: %i" % (n)) 
print ("%s" % format(primes))

# Plot pk versus k * ln (pk)
k_ln_prime = map(lambda p : (primes.index(p)+1) * math.log(p), primes)

x = primes
y = k_ln_prime
plt.plot(x, y)
plt.show()



            
