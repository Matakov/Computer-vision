import numpy as np
import cv2
import math

def subpixelacc(leftimg,rightimg):
	#img_rgb = cv2.imread('mario.png')
	img_graylf = cv2.cvtColor(leftimg, cv2.COLOR_BGR2GRAY)
	img_grayrg = cv2.cvtColor(rightimg, cv2.COLOR_BGR2GRAY)
	
	DbasicSubpixel = np.zeros(img_graylf.shape)
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

			# Construct template and region of interest.
			template = img_grayrg[minr:maxr,minc:maxc]
			templateCenter = [math.floor((template.shape[0]+1)/2),math.floor((template.shape[1]+1)/2)]
			#roi = [minr+templateCenter(1)-2, minc+templateCenter(2)+mind-2, 1, maxd-mind+1]

			templateavg=float(sum(sum(template)))/(template.shape[0]*template.shape[1])
			templatemult=np.subtract(template.astype(float),templateavg)
			templatedown=sum(sum(np.square(templatemult)))


			imagetemplate = img_graylf[minr:maxr,mind+minc:maxd+maxc]
			res = cv2.matchTemplate(imagetemplate,template,cv2.TM_CCORR_NORMED)
			min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
			#print template
			#print imagetemplate
			#print max_loc		

			ix = max_loc[0] + mind
			if max_loc[0]-1 <= 0:
				prev=0
			else:
				prev = res[max_loc[1],max_loc[0]-1]
			if max_loc[0]+1 >= res.shape[1]:
				next=0
			else:
				next = res[max_loc[1],max_loc[0]+1]
			DbasicSubpixel[m,n] = ix - 0.5 * ( next- prev)/(next + prev - 2*res[max_loc[1],max_loc[0]]) 		

	return DbasicSubpixel
