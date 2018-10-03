import numpy as np
import cv2
import math

def blockmatcher_color(leftimg,rightimg):
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
			template_r = leftimg[minr:maxr,minc:maxc][0]
			template_g = leftimg[minr:maxr,minc:maxc][1]
			template_b = leftimg[minr:maxr,minc:maxc][2]
			
			lista = []
			for k in range(mind,maxd):
				template_r2 = rightimg[minr:maxr,(minc+k):(maxc+k)][0]
				template_g2 = rightimg[minr:maxr,(minc+k):(maxc+k)][1]
				template_b2 = rightimg[minr:maxr,(minc+k):(maxc+k)][2]
				#print template_r
				#print template_r2
				diff = sum(sum(abs(template_r-template_r2)))+sum(sum(abs(template_g-template_g2)))+sum(sum(abs(template_b-template_b2)))
				lista.append(diff)
			
			min_loc = lista.index(min(lista))
					

			Dbasic[m,n] = min_loc + mind
		
	#print Dbasic.shape
	return Dbasic

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

def blockmatcher_corr(leftimg,rightimg):
	#img_rgb = cv2.imread('mario.png')
	img_graylf = cv2.cvtColor(leftimg, cv2.COLOR_BGR2GRAY)
	img_grayrg = cv2.cvtColor(rightimg, cv2.COLOR_BGR2GRAY)
	
	Dbasic = np.zeros(img_graylf.shape)
	disparityRange = 15
	# Selects (2*halfBlockSize+1)-by-(2*halfBlockSize+1) block.
	halfBlockSize = 3
	blockSize = 2*halfBlockSize+1
	# Allocate space for all template matchers.
	tmats = np.empty(blockSize, dtype=object)	#tmats = cell(blockSize)

	# Scan over all rows.
	for m in range(0,leftimg.shape[0]):
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
		template = img_grayrg[minr:maxr,minc:maxc]
		templateCenter = [math.floor((template.shape[0]+1)/2),math.floor((template.shape[1]+1)/2)]
		#roi = [minr+templateCenter(1)-2, minc+templateCenter(2)+mind-2, 1, maxd-mind+1]

		templateavg=float(sum(sum(template)))/(template.shape[0]*template.shape[1])
		templatemult=np.subtract(template.astype(float),templateavg)
		templatedown=sum(sum(np.square(templatemult)))
		# Lookup proper TemplateMatcher object; create if empty.
		"""
		if isempty(tmats{size(template,1),size(template,2)}):
		    tmats{size(template,1),size(template,2)} = ...
		        video.TemplateMatcher('ROIInputPort',true);
		"""
		#thisTemplateMatcher = tmats{size(template,1),size(template,2)};

		# Run TemplateMatcher object.
		#loc = step(thisTemplateMatcher, img_graylf, template, roi);
		#res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
		#res.index(max(res))
		
		imagetemplate = img_graylf[minr:maxr,mind+minc:maxd+maxc]
		res = cv2.matchTemplate(imagetemplate,template,cv2.TM_CCORR_NORMED)
    	
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		#print template
		#print imagetemplate
		print max_loc		

		Dbasic[m,n] = max_loc[0] + mind
		
	#print Dbasic.shape
	return Dbasic
	
def blockmatcher_bigcorr(leftimg,rightimg):
	#img_rgb = cv2.imread('mario.png')
	img_graylf = cv2.cvtColor(leftimg, cv2.COLOR_BGR2GRAY)
	img_grayrg = cv2.cvtColor(rightimg, cv2.COLOR_BGR2GRAY)
	
	Dbasic = np.zeros(img_graylf.shape)
	disparityRange = 15
	# Selects (2*halfBlockSize+1)-by-(2*halfBlockSize+1) block.
	halfBlockSize = 3
	blockSize = 2*halfBlockSize+1
	# Allocate space for all template matchers.
	tmats = np.empty(blockSize, dtype=object)	#tmats = cell(blockSize)

	# Scan over all rows.
	for m in range(0,leftimg.shape[0]):
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
		
		mindr = max( -disparityRange, 0-minr )
		maxdr = min( disparityRange, leftimg.shape[0]-maxr )
		
		# Construct template and region of interest.
		template = img_grayrg[minr:maxr,minc:maxc]
		templateCenter = [math.floor((template.shape[0]+1)/2),math.floor((template.shape[1]+1)/2)]
		

		templateavg=float(sum(sum(template)))/(template.shape[0]*template.shape[1])
		templatemult=np.subtract(template.astype(float),templateavg)
		templatedown=sum(sum(np.square(templatemult)))
		
		imagetemplate = img_graylf[mindr+minr:maxr+maxdr,mind+minc:maxd+maxc]
		res = cv2.matchTemplate(imagetemplate,template,cv2.TM_CCORR_NORMED)
    	
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		
		#print max_loc		

		Dbasic[m,n] = max_loc[0] + mind
		
	#print Dbasic.shape
	return Dbasic