# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:13:28 2017

@author: Laila Elbeheiry
@andrew id: loe
@modification history:
    start           end
    24/11 16:13     24/11 17:04 
    
@descr EXTRACTS A FEATURE OF THE IMAGES    
"""
import skimage.io as io
import skimage.transform as transform
from scipy import ndimage as nd
import skimage.feature as feature
import skimage.segmentation as segmentation
import skimage.filters as filters
from PIL import Image

#create a text file to save the features in
f=open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\features\hog.txt", "w")


#loop over all the images
for i in range (1,799):
    #read each image as a numpy array
    i="C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\samples2\\"+str(i)+".png"
    pic=io.imread(i)
    #resize the image
    pic=transform.resize(pic,(50,50))
    #extract its histogram of gradients
    hist=feature.hog(pic)
    #convert the array of hog's into a list
    hist=hist.tolist()
    #write the string of the list in one line of the text file
    hist=str(hist)+"\n"
    f.write(hist)

f.close()
    
    
