#usr/bin/python3
#inport the module of the user math functions
import mathdefs as md
import os

try:
	#Initialize block
	print('Calculate an areas of different figures')
	
	switch = True
	choice = int(input('Press 1 for triangle, \r\n2 for rectangle, \r\n3 for ellipse, \r\n4 for Parallelogram, \r\n5 for trapeze, \r\n6 for sphere, \r\n7 for cylinder, \r\n8 for cube \r\n>>> '))
	
	if ((choice < 1) and (choice > 8)):
		print('The proram was aborted!')
		switch = False
		
	elif (choice == 1): #Load Triangle module
		
		os.system('python triangle.py')
	
	elif (choice == 2): #Load Rectangle module
		
		os.system('python rectangle.py')
	
	elif (choice == 3): #Load Ellipse module
		
		os.system('python ellipse.py')
	
	elif (choice == 4): #Load Parallelogram module
		
		os.system('python parallelogram.py')
	
	elif (choice == 5): #Load Trapeze module
		
		os.system('python trapeze.py')
	
	elif (choice == 6): #Load Cylinder module
		
		os.system('python cylinder.py')
	
	elif (choice == 7):	#Load Sphere module
		
		os.system('python sphere.py')
	
	elif (choice == 8):	#Load Cube module
		
		os.system('python cube.py')

except ZeroDivisionError:
    print('On zero share cannot be!')		
except ValueError:
    print("You have some mistake of userinput Value")
except TypeError:
   print("You have some mistake of type Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )
