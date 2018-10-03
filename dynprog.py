import numpy as np
import cv2
import math
from timeit import default_timer as timer


def dynprog(leftimg,rightimg,disparityRange = 15):
	start = timer()
	#img_rgb = cv2.imread('mario.png')
	img_graylf = cv2.cvtColor(leftimg, cv2.COLOR_BGR2GRAY)
	img_grayrg = cv2.cvtColor(rightimg, cv2.COLOR_BGR2GRAY)

	Ddynamic = np.zeros((img_graylf.shape))
	


	width = img_graylf.shape[1]
	height = img_graylf.shape[0]
	matrix = np.ones((width+1,width+1))*10000
	#// Initialize DP Matrix
	for i in range(width+1):
		if i<disparityRange:
			matrix [0][i] = float(i)
			matrix [i][0] = float(i)
	

	# Scan over all columns.
	for y in range(0,height):
		print y
		for j in range(1,width):
			for i in range(1,width):
				if(abs(i-j)<disparityRange):
					r_i = float(img_grayrg[y][i-1])
					l_i = float(img_graylf[y][j-1])
					#r_r = float(rightimg[y][i-1][0])
					#l_r = float(leftimg[y][j-1][0])
					#r_g = float(rightimg[y][i-1][1])
					#l_g = float(leftimg[y][j-1][1])
					#r_b = float(rightimg[y][i-1][2])
					#l_b = float(leftimg[y][j-1][2])
		    			
					#dif = float(abs(l_r-r_r) + abs(l_g-r_g) + abs(l_b-r_b))
					dif = float(abs(l_i-r_i))
					m00 = matrix[  j-1 ][ i-1 ]
					m01 = matrix[  j   ][ i-1 ]
					m10 = matrix[  j-1 ][ i   ]
	
					add = min(m00,m01)
					add = min(add,m10) 
				
					add = add + dif

					matrix[j][i] = add
		
		# init path position	
		pathX=width-1
		pathY=width-1
		# find Path
		while(( pathX > 0 ) or ( pathY > 0 )):
			# initialize with a big number
			d00 = 10000
		 	d01 = 10000
			d10 = 10000

			# read Matrix 
		 	if(pathX>0):
				if(pathY>0):
					d00=matrix[pathY-1][pathX-1]
			if(pathX>0):  
					d01=matrix[pathY  ][pathX-1]
			if(pathY>0):	
					d10=matrix[pathY-1][pathX  ]
			 
			#// choose new position
			if((d00<=d01)and(d00<=d10)):	
					pathX=pathX-1
					pathY=pathY-1 
					#else // d00 is smallest
			if((d01< d00)and(d01<=d10)):
					pathX=pathX-1  
			else: # // d01 is smallest
					pathY=pathY-1   #// d10 is smallest

			disparity = (pathY-pathX )
			Ddynamic[y][pathX]=disparity
	    
	end = timer()
	print "Time(sec): ",(end - start)
	print np.amax(Ddynamic),np.argmax(Ddynamic)
	print np.amin(Ddynamic),np.argmin(Ddynamic)
	return Ddynamic

	
