#get input
#from gaussian_template import gaussian_template
#from convolvemy import convolve
#from otsu import otsu
#from sobol import sobol
#from reducesize import reducesize
from blockmatcher import blockmatcher_color
from blockmatcher import blockmatcher_gray
from blockmatcher import blockmatcher_corr
from blockmatcher import blockmatcher_bigcorr
from subpixelacc import subpixelacc
from dynprog import dynprog
from smoothing import smoothing


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
print cv2.__version__

from Tkinter import Tk
from tkFileDialog import askopenfilename
from PIL import Image as im
from PIL import Image

from skimage import measure

"""
sigma=1.4
winsize=3

temp,temp2 = gaussian_template(winsize,sigma)
print temp
#print temp2
#print sum(sum(temp2))
gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
gy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

print gx
print gy
"""
"""
#X = range(0,winsize)
#Y = range(0,winsize)
#X,Y = np.meshgrid(X,Y)
#plt.figure()
#ax = Axes3D(plt.gcf())
#ax.plot_wireframe(X,Y,temp)
#plt.show()
"""


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
im = Image.open(filename)#.convert('L')
filename2 = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename2)
im1 = Image.open(filename2)#.convert('L')
#print im
"""
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
frame1_new = cv2.cvtColor(np.array(im),  cv2.COLOR_BGR2GRAY)
frame2_new = cv2.cvtColor(np.array(im1),  cv2.COLOR_BGR2GRAY)
exitpic  = stereo.compute(frame2_new, frame1_new)
"""

#plt.imshow(im)
#plt.show(block=False)
#exitpic = blockmatcher_corr(np.array(im),np.array(im1))
#exitpic = blockmatcher_bigcorr(np.array(im),np.array(im1))
exitpic = blockmatcher_gray(np.array(im),np.array(im1))
#exitpic = blockmatcher_color(np.array(im),np.array(im1))
#exitpic = dynprog(np.array(im),np.array(im1))
#exitpic = smoothing(np.array(im),np.array(im1))
#exitpic = subpixelacc(np.array(im),np.array(im1))
#exitpic = dynprog(np.array(im),np.array(im1))

plt.imshow(exitpic)
plt.show()

"""
ycbcr = im.convert('RGB')
im2= np.array(im)
#np.delete(im2,np.s_[::1],2)
#im2 = np.ndarray((im.size[1], im.size[0], 3), 'u1', im.tobytes())

#print im2

print temp

im3 = convolve(im2,temp)
#im4 = convolve(im3,temp)
#im5 = convolve(im4,temp)
_,image,imN1,imN2 = sobol(im2)

#print im2.shape

#plt.imshow(im2, cmap='Greys_r')
#plt.show()

#all_labels = measure.label(imN1,background=0)
print imN1.shape
imageshow=plt.imshow(imN1)
#plt.show()
#plt.imshow(imN1)
plt.show()
#cv2.imshow(imN1)

pic2 = reducesize(im2)
#plt.imshow(pic2,cmap="Greys_r")
plt.imshow(pic2)
#plt.imshow(im2)
plt.show()
"""

