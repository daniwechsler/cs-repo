#
# CS Problem 7
# Author: Daniel Wechsler
#

import intToWord as word

# We know:
N = 1024384027  # p*q
c = 910510237   # public Key
b = 100156265   # cypertext encripted using c

#
# Compute r using brute force. Just iterate
# over possible r's until it satisfies the condition (2.16)
#

r = 2
while r < N:


    if pow (b, r, N) == 1:
        print ("Found r=%i" % r)
        break
    
    r += 1



# Above method gives r=256080004
power = pow(b, r, N)

#
# Find d' (iterate over possible d's until we reach an
# integer that satisfies c*d'=1 + m*r)
# 
d = 1
r = float(r)
while d < N:
        m = (c * d - 1) / r
        if int(m) == m:
            print("Found d %i" % d)
            d = int(d)
            break
        d += 1


# Compute a from our d' (Found d'=32005)
a = pow(b,d,N)

print("The Word Aclice sent was: %s" % word.intToWord(a))
# Secret word is: eureka



