# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 09:47:09 2017

@author: Laila Elbeheiry
@andrew id: loe
@modification history:
    start           end
    24/11 10:21     24/11 11:02
@desc: The purpose of this code is to take the handwritten samples that I collected from
the students and crop them into letters and save each letter in my samples file    
"""
from PIL import Image
#first I will crop each image from the samples so that the letter touches the borders
#for cropping, I have to find of the letter

#find the first non-white pixel horizontally (beginnig of the letter)
def findBlackX(photo,a,b):
    #loop through the image column by column
    #until a non-white pixel is detected
    for x in range(a):
        for y in range(b):
            if photo.getpixel((x,y))<220:
                return x
 
#find the last non-white pixel horizontally (ending of the letter)       
def findBlackX2(photo,a,b):
    #loop over the image column by column starting from the last column
    #until a non-white pixel is detected
    for x in range(a-1,0,-1):
        for y in range(b):
            if photo.getpixel((x,y))<220:
                return x 
            
            
#find the first non-white pixel vertically (beginning of the letter)       
def findBlackY(photo,a,b):
    #loop over the image row by row 
    #until a non-white pixel is detected
    for y in range(b):
        for x in range(a):
            if photo.getpixel((x,y))<220:
                return y 
            
#find the last non-white pixel vertically (ending of the letter)       
def findBlackY2(photo,a,b):
    #loop over the image row by row starting from the last row
    #until a non-white pixel is detected
    for y in range(b-1,0,-1):
        for x in range(a):
            if photo.getpixel((x,y))<220:
                return y
            
#crop the photo according to the beginning and ending positions of the letter
def cropPhoto(photo,w,h):
    x1=findBlackX(photo,w,h)
    x2=findBlackX2(photo,w,h)
    y1=findBlackY(photo,w,h)
    y2=findBlackY2(photo,w,h)
    return photo.crop((x1,y1,x2,y2))



#loop over all the sample images
for i in range (1,799):
    i=str(i)+".png"
    #open each image
    pic=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\moresamples\uncropped\\"+i)
#    pic.show()
    #convert it to grey scale
    pic=pic.convert("L")
    w,h=pic.size
    #crop the picture
    pic=cropPhoto(pic,w,h)
    #resize to standardize sample sizes for training the classifier
    pic=pic.resize((100,100))
#    pic.show()
    #save the image in a new folder
    pic.save("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\samples2\\"+i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    