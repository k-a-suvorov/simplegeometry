import math
import random

#Processing block

#math fanctions of areas of the geometrical figure
#usr/bin/python3
#An Area of the triangle
def area_triangle(a, h):
	s = (1 / 2) * (a * h)
	return s

#An Area of the rectangle
def area_rectangle(a, b):
	s = a * b
	return s

#An Area of the ellipse		
def area_ellipse(r1, r2):
	s = round(math.pi * (r1 * r2), 2)
	return s

#An Area of the parallelogram	
def area_parallelogram(a, h):
	s = a * h
	return s

#An Area of the trapeze
def area_trapeze(a, b, h):
	s = round(((a + b) / (2 * h)), 2)
	return s

#An Area of the cylinder
def area_cylinder(r, h):
	s = round((2 * math.pi) * (r + h), 2)
	return s

#An Area of the sphere
def area_sphere(r):
	s = round((4 * math.pi) * (r * r), 2)
	return s
