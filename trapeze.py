
import mathdefs as md

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
print(f'The area of the trapeze: {result_trapeze}')
