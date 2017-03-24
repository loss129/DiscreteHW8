import math
import fractions
import random
import time 
import sys
def findprimefactors(n):
	timer = time.time()
	#backup = 2
	factor = 2
	# Start of the while loop to start the algorithm
	print 'Running Without Backup'
	while (factor):				
		# This is my backup method to my attempt to implement Pollard's Rho algorithm
		#if(n%backup == 0):
			#print 'One factor: ', backup
		#	print 'Other factor: ',n/backup
		#	print 'For the number: ', n
		#	print("%s Seconds Elapsed"%(time.time()-timer))
		#	break
		# Incrementing backup so that it gets all the odd numbers from [2,n)
		#else: backup = backup+2
		# Adjustment for adding 2 to 2
		#if (backup == 4):
		#	backup = 3
 #Get a random number within n for x
		x = random.randint(2,n-1)
 #Get a random number within n for r
		r = random.randint(2,n-1)		
	# If the greatest common denomninator is greater than one then we have found a factor 
		factor = fractions.gcd(abs(x-r), n)
		if (factor > 1):
		# We only need one factor in order to find the other so we print the factors and break the while loop
			print 'One factor: ', factor
			print 'Other factor: ',n/factor
			print 'For the number: ', n		
			print("%s Seconds Elapsed"%(time.time()-timer))
			break
# line to take the number from the command line
findprimefactors(int(sys.argv[1]))
	
