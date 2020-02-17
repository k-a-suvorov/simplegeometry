iimport mathdefs as md

#Initialize block
r1 = input('Insert 1st radius of ellipse: ')
r2 = input('Insert 2th radius of ellipse: ')
		
#Processing block

r1 = float(r1)
r2 = float(r2)

if ((r1 == 0) or (r1 < 0) or (r2 == 0) or (r2 < 0)):
	print('The proram was aborted!')
	switch = False		
			
result_ellipse = md.area_ellipse(r1, r2)
		
#Print block
print(f'The area of the ellipse: {result_ellipse}')
