
import mathdefs as md

#Initialize block
		a = input('Insert footing of triangle: ')
		h = input('Insert height of triangle: ')
		
		#Processing block
		a = float(a)
		h = float(h)		
		if ((a == 0) or (h == 0) or (a < 0) or (h < 0)):
			print('The proram was aborted!')
			switch = False
			
		result_triangle = md.area_triangle(a, h)
		
		#Print block
		print(f'The area of the triangle: {result_triangle}')
