# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 19:25:31 2017

@author: Laila
@desc: The purpose of this algorithm is to take the user's handwritten sample
and crop it into letters and save each letter in the user's file
"""
from PIL import Image
import os

folderName=raw_input("what is your name?")
fileName="C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\moresamples\\2017-11-11\\10001.TIF"
os.makedirs("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\"+folderName)

#loop 26 times (once for each letter)
for letter in range(26):
    #open each sample
    pic=Image.open(fileName)
#    pic.show()
    pic=pic.resize((2480,3508))
    
    print pic.size

    #crop it accrding to the letter that is being extracted
    if letter==0:
        pic=pic.crop((1980,100,2380,500)).convert("L").rotate(90)
    elif letter==1:
        pic=pic.crop((1980,620,2380,1020)).convert("L").rotate(90)
    elif letter==2:
        pic=pic.crop((1980,1060,2380,1460)).convert("L").rotate(90)
    elif letter==3:
        pic=pic.crop((1980,1600,2380,2000)).convert("L").rotate(90)
    elif letter==4:
        pic=pic.crop((1980,2090,2380,2490)).convert("L").rotate(90)
    elif letter==5:
        pic=pic.crop((1980,2550,2380,2950)).convert("L").rotate(90)
    elif letter==6:
        pic=pic.crop((1980,3020,2380,3420)).convert("L").rotate(90)
    elif letter==7:
        pic=pic.crop((1300,100,1700,500)).convert("L").rotate(90)
    elif letter==8:
        pic=pic.crop((1300,620,1700,1020)).convert("L").rotate(90)
    elif letter==9:
        pic=pic.crop((1300,1060,1700,1460)).convert("L").rotate(90)
    elif letter==10:
        pic=pic.crop((1300,1600,1700,2000)).convert("L").rotate(90)
    elif letter==11:
        pic=pic.crop((1300,2090,1700,2490)).convert("L").rotate(90)
    elif letter==12:
        pic=pic.crop((1300,2550,1700,2950)).convert("L").rotate(90)
    elif letter==13:
        pic=pic.crop((1300,3020,1700,3420)).convert("L").rotate(90)
    elif letter==14:
        pic=pic.crop((840,100,1240,500)).convert("L").rotate(90)
    elif letter==15:
        pic=pic.crop((840,620,1240,1020)).convert("L").rotate(90)
    elif letter==16:
        pic=pic.crop((840,1060,1240,1460)).convert("L").rotate(90)
    elif letter==17:
        pic=pic.crop((840,1600,1240,2000)).convert("L").rotate(90)
    elif letter==18:
        pic=pic.crop((840,2090,1240,2490)).convert("L").rotate(90)
    elif letter==19:
        pic=pic.crop((840,2550,1240,2950)).convert("L").rotate(90)
    elif letter==20:
        pic=pic.crop((840,3020,1240,3420)).convert("L").rotate(90)
    elif letter==21:
        pic=pic.crop((360,100,760,500)).convert("L").rotate(90)
    elif letter==22:
        pic=pic.crop((360,620,760,1020)).convert("L").rotate(90)
    elif letter==23:
        pic=pic.crop((360,1060,760,1460)).convert("L").rotate(90)
    elif letter==24:
        pic=pic.crop((360,1600,760,2000)).convert("L").rotate(90)
    elif letter==25:
        pic=pic.crop((360,2090,760,2490)).convert("L").rotate(90)
#    pic.show()
    #save the image
    savingNumber=str(letter+1)
    pic.save("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\"+folderName+"\\"+savingNumber+".png")
    

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
for i in range (1,27):
    pho=[]

    photo=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\"+folderName+"\\"+str(i)+".png")
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
    
textfile=open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\"+folderName+"\\"+"featurs.txt","a+")
for sample in samples:
    sample=str(sample)+"\n"
    textfile.write(sample)
textfile.close()

       
    
    
 

