# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:52:43 2017

@author: Beheiry
"""
from PIL import Image



im=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\somethin - Copy\8.png").convert("L")
#
#
#from skimage.restoration import denoise_bilateral
#from skimage import img_as_float
#from scipy import misc
#
#
#pic=misc.imread("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\somethin - Copy\8.png")
#pic=img_as_float(pic)
#pic=denoise_bilateral(pic)
#pic=Image.fromarray(pic,"RGB")
#pic.show()
#
print im.size            
def topSegmentation(pic):
    w,h=pic.size
    for y in range(h):
        for x in range(w):
            c=pic.getpixel((x,y))
            if c<200:
                return y
            
            
def bottomSegmentation(pic,top):
    w,h=pic.size
    for y in range(top,h+1):
        inLine=False
        for x in range(w):
            c=pic.getpixel((x,y))
            if c<200:
                inLine=True
        if inLine==False:
            return y
        


            
            
        




