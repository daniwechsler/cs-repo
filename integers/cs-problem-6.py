#
# CS Problem 6
# Author: Daniel Wechsler
#


import findPrimeNumbers as prime
import math

# Finding Carmichael number using Eratosthenes sieve

N                   = 20000;  # We search for Carmichael numbers lower than N
primes              = prime.findPrimeNumbers(N)
primeNumberIndex    = 0      # Used to keep track of which of the numbers below N are primes   
carmichaelNumbers   = []
for q in range(2, N) :

    if q == primes[primeNumberIndex]: # q is a prime, thus no Carmichael number -> skip it
        primeNumberIndex = primeNumberIndex + 1
        if primeNumberIndex == len(primes):
            break
        continue

    # Check for all coprimes of q 
    isCarmichael = True
    for p in primes:
        if q % p != 0:
            if pow(p, q-1, q) != 1:
                isCarmichael = False
                break
                
    if isCarmichael:
      carmichaelNumbers.append(q)
    
   
                

print ("Carmichael numbers below N are:")
print ("%s" % format(carmichaelNumbers))






