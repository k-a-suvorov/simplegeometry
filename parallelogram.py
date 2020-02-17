
import mathdefs as md

#Initialize block
a = input('Insert width of parallelogram: ')
h = input('Insert height of parallelogram: ')
		
#Processing block
a = float(a)
h = float(h)
		
if ((a == 0) or (h == 0) or (a < 0) or (h < 0)):
	print('The proram was aborted!')
	switch = False
			
result_parallelogram = md.area_parallelogram(a, h)
print(f'The area of the rectangle: {result_parallelogram}')
