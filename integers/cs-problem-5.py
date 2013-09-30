#
# CS Problem 5
# Author: Daniel Wechsler
#

import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import findPrimeNumbers as prime

        
n =  10000
primes = prime.findPrimeNumbers(n)

print ("Primes smaller or equal to: %i" % (n)) 
print ("%s" % format(primes))

# Plot pk versus k * ln (pk)
k_ln_prime = map(lambda p : (primes.index(p)+1) * math.log(p), primes)

x = primes
y = k_ln_prime
plt.plot(x, y)
plt.show()

# Evaluate some values for the zeta Reinmann function
def zetaReinman (primes, z):
   
    prod     = 1
    for p in primes:
        q       = 1/(1-pow(p, -z))            
        prod    = q * prod
  
    return prod        


z = 2
zetaRein = zetaReinman(primes, z)
print ("Zeta Reinmann product of %i is  %.50f" % (z, zetaRein))
z = 10
zetaRein = zetaReinman(primes, z)
print ("Zeta Reinmann product of %i is %.50f" % (z, zetaRein))
z = 16
zetaRein = zetaReinman(primes, z)
print ("Zeta Reinmann product of %i is %.50f" % (z, zetaRein))
z = 22
zetaRein = zetaReinman(primes, z)
print ("Zeta Reinmann product of %i is %.50f" % (z, zetaRein))
z = 30
zetaRein = zetaReinman(primes, z)
print ("Zeta Reinmann product of %i is %.50f" % (z, zetaRein))
z = 40
zetaRein = zetaReinman(primes, z)
print ("Zeta Reinmann product of %i is %.50f" % (z, zetaRein))

            
