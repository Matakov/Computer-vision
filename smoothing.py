import numpy as np
import cv2
import math
from subpixelacc import subpixelacc


def smoothing(im,im1):
	pic = subpixelacc(np.array(im),np.array(im1))
	exitpic = np.zeros((pic.shape))
	dim = exitpic.shape	
	for i in range(0,dim[0]):
		#minr=max(0,i-3)
		#maxr=min(dim[0],i+3)
		for j in range(0,dim[1]):
			minc=max(0,j-3)	
			maxc=min(dim[1],j+3)
			#xos = pic[minr:maxr,j]
			yos = pic[i,minc:maxc]
			exitpic[i,j]=sum(yos)/len(yos)
	return exitpic
