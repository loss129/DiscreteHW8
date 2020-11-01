import math
import fractions
import random
import time 
import sys
import numpy as np

def findprimefactors(n):
	timer = time.time()
	factor = True
	# Start of the while loop to start the algorithm
	while (factor):
 #Get a random number within n for x
		x = random.randint(2,n-1)
 #Get a random number within n for r
		r = random.randint(2,n-1)		
	# If the greatest common denomninator is greater than one then we have found a factor 
		factor = fractions.gcd(np.absolute(x-r), n)
		if (factor > 1):
		# We only need one factor in order to find the other so we print the factors and break the while loop
			print(f'One factor: {factor}')
			print(f'Other factor: {n/factor}')
			print(f'For the number: {n}')		
			print("%s Seconds Elapsed"%(time.time()-timer))
			break
# line to take the number from the command line
findprimefactors(int(60477244035776630857))
	
