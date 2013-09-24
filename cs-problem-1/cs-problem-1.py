# CS-Problem 1:
# Author: Daniel Wechsler

# i) Deadline to switch to 64 bit Systems
# 
# Unix Time stamp counts the seconds elapsed since 1st of January 1970.
#
# In case we use signed integers for time representation, the deadline to change 
# to 64 bit Systems is at Tue Jan 19 03:14:07 2038 UTC. 
# Thus the point in time when all bits of the integer representation are 1 and an addition
# of another 1 leads to an overflow.
# 
# In case we use unsigned integers for time representation the deadline is 
# Tue Jan 19 04:13:07 2038 UTC
#

from time import ctime
print "Problem 1.1\n"

maxIntSigned = pow(2, 31) - 1;
print("Max 32 bit signed integer: %i  " % (maxIntSigned))
print("Max representable UNIX time using 32 bit signed integer: %s" % (ctime(maxIntSigned)))


maxIntUnsigned = pow(2, 32) - 1;
print("Max 32 bit unsigned integer: %i  " % (maxIntUnsigned))
print("Max representable using 32 bit unsigned integer: %s" % (ctime(maxIntUnsigned)))


# ii) Representation of floating-point numbers:
# 
# How many bits are used to store the mantissa and exponent?
#
# For double precission (64 bit):
#
# 64 bit (double)
# Mantissa: 52 bit (memory used) implicitly 53 bit -> first bit of normalized number (hidden bit)	 	
# Exponent: 11 bit 
# +1-Bit Sign
# 
# 32 bit (float)
# Mantissa: 23 bit	
# Exponent: 8 bit
# +1-Bit Sign
# (According to IEEE 754)












