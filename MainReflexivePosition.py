#!/usr/bin/python

from ReflexivePosition import ReflexivePosition

if __name__ == "__main__":

	reflPosn = ReflexivePosition()

	# These are examples from the problem statement itself
        print 'reflexive position of 1, should equal 1            : ', reflPosn.f(1) == 1
        print 'reflexive position of 5, should equal 81           : ', reflPosn.f(5) == 81
        print 'reflexive position of 12, should equal 271         : ', reflPosn.f(12) == 271
        print 'reflexive position of 7780, should equal 111111365 : ', reflPosn.f(7780) == 111111365

	# This is the sum of reflexive positions of the function 3^k when k goes from 1 to 13.  It also shows the sums along the way
	total = 0
        for k in range (1, 14):
            
            total += reflPosn.f(3 ** k)
	    print 'sum of reflexive positions of 3^k 1<=k<=13, after k = ', k, ', total = ', total

