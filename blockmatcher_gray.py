import numpy as np
import cv2
import math

def blockmatcher_gray(leftimg,rightimg):
	#img_rgb = cv2.imread('mario.png')
	img_graylf = cv2.cvtColor(leftimg, cv2.COLOR_BGR2GRAY)
	img_grayrg = cv2.cvtColor(rightimg, cv2.COLOR_BGR2GRAY)
	
	Dbasic = np.zeros(img_graylf.shape)
	disparityRange = 15
	# Selects (2*halfBlockSize+1)-by-(2*halfBlockSize+1) block.
	halfBlockSize = 3
	blockSize = 2*halfBlockSize+1
	
	# Scan over all rows.
	for m in range(0,leftimg.shape[0]):
		print m
		# Set min/max row bounds for image block.
		minr = max(0,m-halfBlockSize)
		maxr = min(leftimg.shape[0],m+halfBlockSize)
		# Scan over all columns.
		for n in range(0,leftimg.shape[1]):
			minc = max(0,n-halfBlockSize)
			maxc = min(leftimg.shape[1],n+halfBlockSize)
			# Compute disparity bounds.
			mind = max( -disparityRange, 0-minc )
			maxd = min( disparityRange, leftimg.shape[1]-maxc )
			"""
			print "M: ",m
			print "N: ",n
			print minc
			print maxc
			print mind
			print maxd
			"""
			# Construct template and region of interest.
			template1 = img_graylf[minr:maxr,minc:maxc]
			
			lista = []
			for k in range(mind,maxd):
				template2 = img_grayrg[minr:maxr,(minc+k):(maxc+k)]
				diff = sum(sum(abs(template1-template2)))
				lista.append(diff)
			
			min_loc = lista.index(min(lista))

			Dbasic[m,n] = min_loc + mind
		
	#print Dbasic.shape
	return Dbasic

