import mathdefs as md
try:
	
		#Initialize block
	a = float(input('Insert width of Rectangle: '))
	b = float(input('Insert height of Rectangle: '))
		
	result_perimeter = md.perimeter_rect(a,b)
	result_area = md.area_rect(a,b)
	result_diagonal = md.diagonal_rect(a,b)
		
		#Print block
	print(f'The perimeter of the rectangle: {result_perimeter}')
	print(f'The area of the rectangle: {result_area}')
	print(f'The diagonal of the rectangle: {result_diagonal}')

except ValueError:
    print("You have some mistake of userinput current float Value")
except TypeError:
   print("You have some mistake of userinput float Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )
