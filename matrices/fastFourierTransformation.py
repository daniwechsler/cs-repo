from numpy import pi, array, ndarray
import cmath

#
# Computes the discrete Fourier transform (DFT) using 
# fast Fourier transform (FFT). The input list's length
# should be a power of 2.
#
def fastFourierTransformation (f) :
    n = len(f)

    # If n reachd 1 we can not divide the problem any further
    if n==1 :
        return f
    else :
        # Compute lists of odd and even elements (index) of f
        evenElements = f[::2]
        oddElements  = f[1::2]

        # Recursice call with elements split in odd and even
        even    = fastFourierTransformation (evenElements)
        odd     = fastFourierTransformation (oddElements)
        c       = array(range(n), complex)
        
        for k in range (0, n/2) :
            c[k]     = even[k] + odd[k] * cmath.exp(-2*pi*k*complex(0,1) / n)
            c[k+n/2] = even[k] - odd[k] * cmath.exp(-2*pi*k*complex(0,1) / n)

        return c
    
