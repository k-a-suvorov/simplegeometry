
import mathdefs as md

#Initialize block
a = input('Insert width of rectangle: ')
b = input('Insert height of rectangle: ')
		
#Processing block
a = float(a)
b = float(b)
if ((a == 0) or (b == 0) or (a < 0) or (b < 0)):
	print('The proram was aborted!')
	switch = False
			
result_rectangle = md.area_rectangle(a, b)
		
#Print block
print(f'The area of the rectangle: {result_rectangle}')
