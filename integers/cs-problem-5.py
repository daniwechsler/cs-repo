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



            
