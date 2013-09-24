# CS-Problem 2:
# Author: Daniel Wechsler

#
# Given x >= 0 and n [Integer] the function computes the n-th root of x using the
# Newton-Raphson method.
#
# Idea:
# y = nroot(x, n)
# 
# f(y) = y^n-x		(We want y where f(y) = 0)
# 

def nroot (x, n=2):
	
	# Abort if x is less than 0
	if x < 0:
		return None
	
	guess			= 1						# We make an initial guess of the result (starting point for Newton-Raphson algorithm - could be optimized)
	error			= None					# Holds the error of previous iteration

	while True: 
		
		# Compute next guess using current guess (Newton-Raphson method)
		dividend 		= (n-1) * pow(guess,n) + x
		divisor 		= (n * pow(guess, n-1))
		currentGuess	= float(dividend) / float(divisor)

		# Compute error |guess^n - x| 	
		currentError	= abs(pow(currentGuess, n) - x)

		# Due to finite precision the algorithm can not be expected to converge to a steady point (It converges to a cycle) 
		# We compare the current error with the one we computed at previous iteration. 
 		# In case the previous error is smaller or same, maximum precision is reached. Thus we return the guess from previous iteration.

		if error != None: # Don't compare if no initial error is known (initial guess might be better than first iteration result of algorithm).
			if  currentError >= error:
				return guess

		guess 	= currentGuess
		error	= currentError
			
	return y;



print("Function %f" % nroot(90,5))


