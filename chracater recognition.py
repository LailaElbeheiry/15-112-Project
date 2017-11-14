"""
Created on Thu Nov 09 23:16:13 2017

@author: Laila
@desc: This is the code for recognizing the handwritten characters
@DISCLAIMER: the code is 92% accurate in recognizing hnadwritten samples according the classification score
I have used 15 samples for each lowercase letter and 7 samples for each digit from 0 to 9
As I keep adding samples, I keep changing this code

"""


from PIL import Image
from sklearn.neural_network import MLPClassifier
import numpy as np

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




photo=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\Nahin.jpg")


w= photo.size[0]
h=photo.size[1]
photo=photo.convert("L")
#photo.show()
photo=cropPhoto(photo,w,h)
test=[]
photo=photo.resize((100,100))
#photo.show()

for x in range(100):
    for y in range(100):
        if photo.getpixel((x,y))>200:
            test.append(1)
        else:
            test.append(0)
picture=np.array(test).reshape(1,-1)

        

count=0
#values=[]
#comparison=[]
samples=[]

#for i in range (71,253):
#    pho=[]
#
#    photo=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\mysamples\\"+str(i)+".png")
#    w,h=photo.size
#    photo=photo.convert("L")
#    photo=cropPhoto(photo,w,h)
#    photo=photo.resize((100,100))
#    
#    for x in range(100):
#        for y in range(100):
#            if photo.getpixel((x,y))>200:
#                pho.append(1)
#            else:
#                pho.append(0)
#    samples.append(pho)
targets=[]
strings="1234567890"
for i in strings:
    for x in range(7):
        targets.append(i)
strings="abcdefghijklmnopqrstuvwxyz"
for i in strings:
    for x in range(7):
        targets.append(i)
        
for i in strings:
    for x in range(8):
        targets.append(i)
for i in strings:
    targets.append(i)


sampleImages=[]
textfile=open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\my.txt","r")
for i in range(1,487):
    
    sample=textfile.readline()
    sample=eval(sample)
    sampleImages.append(sample)
clf = MLPClassifier()
clf.fit(sampleImages,targets)
print clf.predict(picture)


#testingImages=[]
#for i in range(1,27):
#    photo=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\moresamples\\2017-11-11\\tests\\"+str(i)+".png")
#
#
#    w= photo.size[0]
#    h=photo.size[1]
#    photo=photo.convert("L")
#    #photo.show()
#    photo=cropPhoto(photo,w,h)
#    test=[]
#    photo=photo.resize((100,100))
#    #photo.show()
#    
#    for x in range(100):
#        for y in range(100):
#            if photo.getpixel((x,y))>200:
#                test.append(1)
#            else:
#                test.append(0)
#    testingImages.append(test)
#    
#testingTargets=list("abcdefghijklmnopqrstuvwxyz")
#
#print clf.score(testingImages,testingTargets)


    
#    for l in targets:
#        comparison.append(compareLists(l,test))
# 
#    
#winningList=[]
#for i in range(1,8):
#    count=0
#    index=1
#    for k in range(i,253,7):
#        if comparison[k]>count:
#            count=comparison[k]
#            won=index
#        index+=1
#    winningList.append(won)
#print winningList   
        
    
