"""
Created on Thu Nov 09 23:16:13 2017

@author: Laila
@desc: This code reads all the sample images and converts them to lists and save the lists into a file
@DISCLAIMER: this code keeps changing to add more samples
"""


from PIL import Image

#first I will crop each image from the samples so that the letter touches the borders
#for cropping, I have to find of the letter

#find the first non-white pixel horizontally (beginnig of the letter)
def findBlackX(a,b):
    #loop through the image column by column
    #until a non-white pixel is detected
    for x in range(a):
        for y in range(b):
            if photo.getpixel((x,y))<128:
                return x
 
#find the last non-white pixel horizontally (ending of the letter)       
def findBlackX2(a,b):
    #loop over the image column by column starting from the last column
    #until a non-white pixel is detected
    for x in range(a-1,0,-1):
        for y in range(b):
            if photo.getpixel((x,y))<128:
                return x 
            
            
#find the first non-white pixel vertically (beginning of the letter)       
def findBlackY(a,b):
    #loop over the image row by row 
    #until a non-white pixel is detected
    for y in range(b):
        for x in range(a):
            if photo.getpixel((x,y))<128:
                return y 
            
#find the last non-white pixel vertically (ending of the letter)       
def findBlackY2(a,b):
    #loop over the image row by row starting from the last row
    #until a non-white pixel is detected
    for y in range(b-1,0,-1):
        for x in range(a):
            if photo.getpixel((x,y))<128:
                return y
            
#crop the photo according to the beginning and ending positions of the letter
def cropPhoto(photo,w,h):
    x1=findBlackX(w,h)
    x2=findBlackX2(w,h)
    y1=findBlackY(w,h)
    y2=findBlackY2(w,h)
    return photo.crop((x1,y1,x2,y2))



samples=[]
for i in range (461,487):
    pho=[]

    photo=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\mysamples\\"+str(i)+".png")
    w,h=photo.size
    photo=photo.convert("L")
    photo=cropPhoto(photo,w,h)
    photo=photo.resize((100,100))

    
    for x in range(100):
        for y in range(100):
            if photo.getpixel((x,y))>200:
                pho.append(1)
            else:
                pho.append(0)
    samples.append(pho)
    
textfile=open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\my.txt","a")
for sample in samples:
    sample=str(sample)+"\n"
    textfile.write(sample)
textfile.close()
