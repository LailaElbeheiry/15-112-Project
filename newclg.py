# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:45:30 2017

@author: Beheiry
"""

from sklearn.neural_network import MLPClassifier
import skimage.io as io
import skimage.feature as feature
import skimage.transform as transform
import numpy as np

"""The code has already been implements
And the neural network classifier has been trained
now this code only loads the trained classifier"""

#testingImages=[]
#for i in range (1,53):
#    i="C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\test\\"+str(i)+".png"
#    pic=io.imread(i)
#    pic=transform.resize(pic,(50,50))
#    dz=feature.daisy(pic)
#    dz=dz.ravel()
#    dz=dz.tolist()
#    histo=feature.hog(pic)
#    histo=histo.tolist()
#    allfeatures=dz+histo    
#    testingImages.append(allfeatures)    
#    
#    
#sampleImages=[]
#textfile=open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\features\\daisy.txt","r")
#textfile2=open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\features\\hog.txt","r")
#for i in range(1,799):
#    
#    sample=textfile.readline()
#    sample=eval(sample)
#    sample2=textfile2.readline()
#    sample2=eval(sample2) 
#    all=sample+sample2
#    sampleImages.append(all)
#    
#sampletargets=[]
#strings="1234567890"
#for i in strings:
#    for x in range(7):
#        sampletargets.append(i)
#lowerCstrings="abcdefghijklmnopqrstuvwxyz"
#upperCstrings="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#for i in lowerCstrings:
#    for x in range(7):
#        sampletargets.append(i)
#        
#for i in lowerCstrings:
#    for x in range(8):
#        sampletargets.append(i)
#for i in lowerCstrings:
#    sampletargets.append(i)
#for i in lowerCstrings:
#    for x in range(12):
#        sampletargets.append(i)
#    
#testingtargets=[]
#for i in lowerCstrings:
#    for x in range(2):
#        testingtargets.append(i)
#
#clf= MLPClassifier()
#clf.fit(sampleImages,sampletargets)
#print clf.score(testingImages,testingtargets)


def predictPic(fileName):
    #load the picture as an array
    pic=io.imread(fileName)
    #resize it
    pic=transform.resize(pic,(50,50))
#    Extract its features (daisy and hog)
    dz=feature.daisy(pic)
    dz=dz.ravel()
    dz=dz.tolist()
    histo=feature.hog(pic)
    histo=histo.tolist()
    allfeatures=dz+histo    
    allfeatures=np.array(allfeatures)
    allfeatures=allfeatures.reshape(1,-1)
    #predict an image and return the detected letter
    letter= clf.predict(allfeatures) 
    letter=letter.tolist()
    return letter
    
    
    
#    
from sklearn.externals import joblib
#joblib.dump(clf, 'C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\classifiers\MLPClassifier2.pkl')
clf = joblib.load('C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\classifiers\MLPClassifier2.pkl')   
    
    
    
    
