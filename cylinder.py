
import mathdefs as md

#Initialize block
r = input('Insert radius of cylinder: ')
h = input('Insert height of cylinder: ')
		
#Processing block
r = float(r)
h = float(h)
if ((r == 0) or (h == 0) or (r < 0) or (h < 0)):
	print('The proram was aborted!')
	switch = False
			
result_cylinder = md.area_cylinder(r, h)
		
	#Print block
print(f'The area of the cylinder: {result_cylinder}')
