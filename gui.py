from Tkinter import *
import tkMessageBox
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2

from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory
from PIL import Image as im
from PIL import Image

#get input
#from gaussian_template import gaussian_template
#from convolvemy import convolve
#from otsu import otsu
#from sobol import sobol
#from reducesize import reducesize
from blockmatcher import blockmatcher
from subpixelacc import subpixelacc
from dynprog import dynprog

from os import listdir
from os.path import isfile, join

OPTIONS = [
    "Block matching",
    "Block matching with subpixel accuracy",
    "Dynamic programming",
    "Image Pyramiding"
]
filenameleft = '-'
filenameright = '-'

def Load():
	global filenameleft
	global filenameright
	if PUT.get()=='File':
		filenameleft = askopenfilename()
		filenameright = askopenfilename()
	else:
		filenameleft = askdirectory()
		filenameright = askdirectory()	
		#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	print filenameleft
	print filenameright

def Run():
	if variableOption.get()=='-':
		print "Molimo Vas izaberite nacin racunanja dubine.\n"
	if variableOption.get()=='Block matching':
		if PUT.get()=='File':
			exitpic = blockmatcher(np.array(Image.open(filenameleft)),np.array(Image.open(filenameright)))
			result = Image.fromarray(exitpic.astype(np.uint8))
			result.save(filenameleft+"_result.jpg")
			print "DONE"
		else:
			onlyfilesleft = [f for f in listdir(filenameleft) if isfile(join(filenameleft, f))]
			onlyfilesright = [f for f in listdir(filenameright) if isfile(join(filenameright, f))]
			for left,right in zip(onlyfilesleft,onlyfilesright):
				exitpic = blockmatcher(np.array(Image.open(filenameleft)),np.array(Image.open(filenameright)))
				result = Image.fromarray(exitpic.astype(np.uint8))
				result.save(filenameleft+"_result.jpg")
			print "DONE"
		
	if variableOption.get()=='Block matching with subpixel accuracy':
		if PUT.get()=='File':
			exitpic = subpixelacc(np.array(Image.open(filenameleft)),np.array(Image.open(filenameright)))
			result = Image.fromarray(exitpic.astype(np.uint8))
			result.save(filenameleft+"_result.jpg")
			print "DONE"
		else:
			onlyfilesleft = [f for f in listdir(filenameleft) if isfile(join(filenameleft, f))]
			onlyfilesright = [f for f in listdir(filenameright) if isfile(join(filenameright, f))]
			for left,right in zip(onlyfilesleft,onlyfilesright):
				exitpic = subpixelacc(np.array(Image.open(filenameleft)),np.array(Image.open(filenameright)))
				result = Image.fromarray(exitpic.astype(np.uint8))
				result.save(filenameleft+"_result.jpg")
			print "DONE"
	"""	OVO SE MORA ZAVRSITI ALI PRVO NAPISATI TE POTPROGRAME
	if variableOption.get()=='Dynamic programming':
		if PUT.get()=='File':

		else:

		
	if variableOption.get()=='Image Pyramiding':
		if PUT.get()=='File':

		else:
	"""
		
	pass


master = Tk()

variableOption = StringVar(master)
variableOption.set('-') # default value
"""
variablePolaziste = StringVar(master)
variablePolaziste.set('-') # default value
variableOdrediste = StringVar(master)
variableOdrediste.set('-') # default value
#variableGorivo= StringVar(master)
#variableGorivo.set('-') # default value
"""

PUT = StringVar()
C1 = Radiobutton(master, text = 'File', variable=PUT, value= 'File',indicator=1)
C2 = Radiobutton(master, text = 'Folder', variable=PUT, value= 'Folder',indicator=1)
C1.select()

Opcije = OptionMenu(master, variableOption, *OPTIONS)
Opcije_Label = Label(master, text="Odaberi nacin racunanja mape dispariteta:")

#Potrosnja=Scale(master, from_=0, to=20, bd=4, orient=HORIZONTAL,resolution = 0.1,length=300, label='Potrosnja(L po 100km)')

Izracunaj = Button(master,text='Izracunaj',command= Run)
#text = Text(master,height=5,width=50)
LoadPicture = Button(master,text='Otvori',command= Load)

Opcije_Label.grid(row=0,column=0)
Opcije.grid(row=0, column=1)
C1.grid(row=1, column=0)
C2.grid(row=1, column=1)
LoadPicture.grid(row=2, columnspan=2)
Izracunaj.grid(row=3,columnspan=2)
#Odrediste_Label.grid(row=1, column=0)
#Odrediste.grid(row=1, column=1)
#Gorivo.grid(row=4, column=1)
#Gorivo_Label.grid(row=4, column=0)
#Potrosnja.grid(row=5,columnspan=2)
#text.grid(row=7,columnspan=2)

mainloop()
