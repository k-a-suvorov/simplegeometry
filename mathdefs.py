import math
import random

#Processing block
def perimeter_rect(a, b):
	p = 2 *(a + b)
	return p
	
def area_rect(a, b):
	s = a * b
	return s
		
def diagonal_rect(a, b):
	d = round(math.sqrt((a * a) + (b * b)), 3)
	return d	
		
