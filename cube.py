
import mathdefs as md

#Initialize block
a = input('Insert width of cube: ')
		
#Processing block
a = float(a)
if ((a == 0) or (a < 0)):
	print('The proram was aborted!')
	switch = False		
			
	result_cube = md.area_cube(a)
		
	#Print block
print(f'The area of the sphere: {result_cube}')
