#inport the module of the user math functions
import mathdefs as md
try:
	#Initialize block
	print('Calculate the areas of different figures')
	
	switch = True
	choice = int(input('Press 1 for triangle, \r\n2 for rectangle, \r\n3 for ellipse, \r\n4 for Parallelogram, \r\n5 for trapeze, \r\n6 for sphere, \r\n7 for cylinder \r\n>>> '))
	
	if ((choice < 1) and (choice > 7)):
		print('The proram was aborted!')
		switch = False
		
	elif (choice == 1):
		
		#Initialize block
		a = input('Insert footing of Triangle: ')
		h = input('Insert height of Triangle: ')
		
		#Processing block
		a = float(a)
		h = float(h)		
		if ((a == 0) or (h == 0) or (a < 0) or (h < 0)):
			print('The proram was aborted!')
			switch = False
			
		result_triangle = md.area_triangle(a, h)
		
		#Print block
		print(f'The area of the triangle: {result_triangle}')
	
	elif (choice == 2):
		
		#Initialize block
		a = input('Insert width of Rectangle: ')
		b = input('Insert height of Rectangle: ')
		
		#Processing block
		a = float(a)
		b = float(b)
		if ((a == 0) or (b == 0) or (a < 0) or (b < 0)):
			print('The proram was aborted!')
			switch = False
			
		result_rectangle = md.area_rectangle(a, b)
		
		#Print block
		print(f'The area of the rectangle: {result_rectangle}')
	
	elif (choice == 3):
		
		#Initialize block
		r1 = input('Insert 1th radius of Ellipse: ')
		r2 = input('Insert 2th radius of Ellipse: ')
		
		#Processing block
		r1 = float(r1)
		r2 = float(r2)
		if ((r1 == 0) or (r2 == 0) or (r1 < 0) or (r2 < 0)):
			print('The proram was aborted!')
			switch = False
			
		result_ellipse = md.area_ellipse(r1, r2)
		
		#Print block
		print(f'The area of the rectangle: {result_ellipse}')
	
	elif (choice == 4):
		
		#Initialize block
		a = input('Insert width of Parallelogram: ')
		h = input('Insert height of Parallelogram: ')
		
		#Processing block
		a = float(a)
		h = float(h)
		
		if ((a == 0) or (h == 0) or (a < 0) or (h < 0)):
			print('The proram was aborted!')
			switch = False
			
		result_parallelogram = md.area_parallelogram(a, h)
		print(f'The area of the rectangle: {result_parallelogram}')
	
	elif (choice == 5):
		
		#Initialize block
		a = input('Insert width of Trapeze: ')
		b = input('Insert width of Trapeze: ')
		h = input('Insert height of Trapeze: ')
		
		#Processing block
		a = float(a)
		b = float(b)
		h = float(h)
		if ((a == 0) or (b == 0) or (h == 0)):
			
			print('The proram was aborted!')
			switch = False
			
		if ((a < 0) or (h < 0) or (b < 0)):
			print('The proram was aborted!')
			switch = False	
			
		result_trapeze = md.area_trapeze(a, b, h)
		
		#Print block
		print(f'The area of the rtrapeze: {result_trapeze}')
	
	elif (choice == 6):
		
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
	
	elif (choice == 7):	
		
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
		
except ValueError:
    print("You have some mistake of userinput Value")
except TypeError:
   print("You have some mistake of type Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )
