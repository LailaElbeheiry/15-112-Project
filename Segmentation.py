# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:52:43 2017

@author: Laila Elbeheiry
@andrew id: loe
@modification history:
    start           end
    11/11 22:52     12/11 03:32 
    25/11 10:03     25/11 15:43
"""
from PIL import Image
import prep
import newclg


#returns the y position of beginning of blob
def findFirstY(pixels,y,w,h):
    #loop through each row from specified row to the end
    for b in range(y,h):
        for a in range(w):
            #if pixel is black then blob has started
            if pixels[a,b]<200:
                return b
    else: return "done"
    

#returns the y position of ending of blob
def findLastY(pixels,y,w,h):
    #loop through each row from specified row to the end
    for b in range(y,h):
        inLine=False
        for a in range(w):
            #if the row has a black pixel then blob hasn't ended
            if pixels[a,b]<200:
                inLine=True
        #if the row has no black pixels then blob has ended
        if inLine==False:
            return b-1
        
    
#returns the y coordinates of beginning and ending of each line in a pic
def lineSegmentation(im):
    w,h=im.size
    #load pixels
    pixels=im.load()
    LinesCoords=[]
    y=0
    #keep executing until all lines are segmented
    while findFirstY(pixels,y,w,h)!="done":
        #find beginning and ending y coordinates of each line
        top=findFirstY(pixels,y,w,h)
        bottom=findLastY(pixels,top+1,w,h)
        LinesCoords.append((top,bottom))
        y=bottom+1
    return LinesCoords



#returns x coordinate of beginning of blob
#loop through each column starting from a specified column
def findFirstX(pixels,start,w,h):
    for a in range(start,w):
        for b in range(h):
            #if the column has a black pixel return its x coordinate
            if pixels[a,b]<200:
                return a
    else: return "done"
    
    
#returns x coordinate of ending of blob
#loop through each column starting from a specified column    
def findLastX(pixels,w,h,x):
    for a in range(x,w):
        inLetter=False
        for b in range(h):
            #if column has a black pixel then its still in the blob
            if pixels[a,b]<200:
                inLetter=True
        #if column has no black pixels than the previous column is the last col
        if inLetter==False:
            return a-1        
 
    
#returns x coordinates of beginning and ending of each letter in a line    
def characterSegmentation(im):
    w,h=im.size
    pixels=im.load()
    CharsCoords=[]
    start=0
    #loop through the line until there are no remaining letters
    while findFirstX(pixels,start,w,h)!="done":
        #find the beginning of the letter
        beg=findFirstX(pixels,start,w,h)
        #find the ending of a letter
        end=findLastX(pixels,w,h,beg+1)
        #append the coordinates to a list
        CharsCoords.append((beg,end))
        #skip this letter
        start=end+1
    return CharsCoords




        
#This is the main function
#it takes a filename of an image as an input
#and returns the converted text as a string
def segPic(fileName, NLD="automatic"):
    #open the image in grey scale mode
    im=Image.open(fileName).convert("L")
    w,h=im.size
    #get the y coordinates of the top and bottom of each line in the image
    lines= lineSegmentation(im)
    #initialize the rest of the variables
    segLines={}
    i=0
    recognizedLines={}
    wholetext=[]
    NLDtext=[]
    #loop over all the lines
    for line in lines:
        #find the coordinates of all the characters in that line
        #by cropping the image at that line
        #and save the character coordinates into a dictionary with value equal to the line number
        segLines[i]=characterSegmentation(im.crop((0,line[0],w,line[1])))
        i+=1
    num=0        
    #now loop over every character in the image
    for l in range(len(lines)):
        letters=[]
        seg=segLines[l]
        for c in seg:
            x1,x2=c
            y1,y2=lines[l]
            #crop the image at that character
            im1=im.crop((x1,y1,x2,y2))
            #and save that image for the character recognition step                        
            im1.save("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\recognition\pic"+str(num)+".png")
            #recrop the image in a way that matches the standard images that were used in the training set
            #that is, the boundaries of each character are touching the border of the image
            prep.prepPic("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\recognition\pic"+str(num)+".png")
            #use the classifier to prdeict the character and append the prediction to a list
            letters.extend(newclg.predictPic("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\\recognition\pic"+str(num)+".png"))
            num+=1
        #append the list of all characters in a line to a dictionary with the value equal to the line number
        recognizedLines[l]=letters
     
    #This part of the function determines whether two characters are 
    #in the same word or in two different words
                              
    diff={}
    #loop over the dictionary of characters coordinates
    for i in range(len(segLines)):
        diffsPerLine=[]
        coords=segLines[i]
        #find the difference between the last coordinate of a letter and the first coordinate of the neighboring one
        #that is find the space between characters
        for n in range(len(coords)-1):
            #put all the spaces between characters in a list
            diffsPerLine.append(coords[n+1][0]-coords[n][1])
        #put the whole list in a dictionary with the value equal to the line number
        diff[i]=diffsPerLine
    #now we have a dictionary with all the spaces between characters in each line
    #make sure the line has more than one word
    #a line with less than eight characters is considered as a one-word-line
    if findAverageWordLetter(diff):
        #if line has more than one word
        #find average space between adjacent words and average space between adjacent characters
        word, letter=findAverageWordLetter(diff)
        indices={}
        #now loop over the dictionary that had spaces between characters for each line
        for i in range(len(diff)):
            #consider the spaces between characters in each line
            indicesOfLine=[]
            toCompare=diff[i]
            for n in range(len(toCompare)):
                #compare the value of each sppace with the average values of words' spaces
                #and letters' spaces
                #if the space is closer to the average word space
                #append the index of that character in order to be able to put a space after it
                if compare(toCompare[n],word,letter)=="word":
                    indicesOfLine.append(n+1)
            #put the indices where spaces need to be put in each line to a dictionary
            #where the value is equal to the line number
            indices[i]=indicesOfLine
    else:
        #if line has less than eight characters consider it as one word
        indices[i]=="word"  
    #loop over the dictionary of indices if spaces in each line
    for i in indices:
        #if there were no spaces (one word)
        if indices[i]=="word":
            #append the whole line to a list
            wholetext.append(recognizedLines[i])
        else:
            #if there were spaces
            #find the spaces of each line
            spaces=indices[i]
            #get the list of recognized characters in that line
            currentLine=recognizedLines[i]
            a=0
            #loop over all the indices of the spaces
            #and split the list at the indices of the spaces
            #this will produce smaller lists where each list represents characters in a single word
            for x in spaces:
                wholetext.append( currentLine[a:x])
                a=x
            wholetext.append( currentLine[x:])
    #now we have a big list containing smaller lists where each list represents the characters of a word
    wordIndex=0    
    #loop over the list of all words    
    for i in wholetext:
        #for each list of characters, join them into one word
        i="".join(i)
        #return the string to the list of words 
        wholetext[wordIndex]=i
        wordIndex+=1
    
    
    #This part of the code depends on the user's preference on New Line Detections
    #if user wants to ignore lines in his image
    if NLD=="off":
        #then join all the words into one string and return it
        wholetext=" ".join(wholetext)
        return wholetext  
    #if user wants new lines in his image to be detected
    else:
        #find the number of words in each line
        #by adding one to the number of spaces in each line
        for i in indices:
            lineLength=len(indices[i])+1
            #cut the whole text into individual lists of words
            #where each list represents one line
            NLDtext.append (wholetext[:lineLength])
            wholetext=wholetext[lineLength:]
        #finally loop over each list of words in a line
        finalNLDtext=""
        for i in NLDtext:
            #join the words into a string and add a new line at the end
            finalNLDtext+=" ".join(i)+"\n"
        return finalNLDtext
            

#this function compares the space between two characters with the 
#average word space and average letter spaces
def compare(difference,word,letter):
    #if difference between word space average and space is greater than
    #the difference between letter space average and space
    #then return letter otherwise return word
    if abs(word-difference)>abs(letter-difference):
        return "letter"
    else:
        return "word"
 
    
#this function finds the average word space and average letter space
def findAverageWordLetter(diff):
    maximum=[]
    minimum=[]
    count=0
    for i in range(len(diff)):
        if len(diff[i])>8:
            #append the maximum and minimum values in the list of spaces between characters
            #to a list representing max values and a list representing min values respectivel
            maximum.append(max(diff[i]))
            minimum.append(min(diff[i]))
        else:
            count+=1
    if count==len(diff):
        return 
    #return average of maximum and average of minimum
    return (sum(maximum)*1.0/len(maximum),sum(minimum)*1.0/len(minimum))

    
                
