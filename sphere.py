
import mathdefs as md

#Initialize block
r = input('Insert radius of sphere: ')
		
#Processing block
r = float(r)
if ((r == 0) or (r < 0)):
	print('The proram was aborted!')
	switch = False		
			
result_sphere = md.area_sphere(r)
		
#Print block
print(f'The area of the sphere: {result_sphere}')
