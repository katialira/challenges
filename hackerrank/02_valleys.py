import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	v = 0
	sea = 0
	last = 0

	for step in s:
		last = sea
		if step == 'U':
			sea +=1
		else:
			sea -=1

		if sea == -1 and last == 0:
			v += 1

	return v

if __name__ == '__main__':

    print(countingValleys(8, 'UDDDUDUU'))
    print(countingValleys(12, 'DDUUDDUDUUUD'))
