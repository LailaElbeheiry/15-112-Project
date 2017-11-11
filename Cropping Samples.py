# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 23:16:13 2017

@author: Laila
@desc: The purpose of this algorithm is to take the handwritten samples that I collected from
the students and crop them into letters and save each letter in my samples file
@DISCLAIMER: this code isn't fully automated as I had to keep changing the folder paths etc.
"""
from PIL import Image

#get the number of samples and the number of the last saved sample
NumberofSamples=int(raw_input("number of samples?"))
lastSaved=int(raw_input("last saved?"))  



#loop 26 times (once for each letter)
for letter in range(26):
    #create a loop with the number of repitions to get all samples
    for rep in range(1,NumberofSamples+1):
        fileNumber=str(10000+rep)
        fileName="C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\moresamples\\2017-11-11\\"+fileNumber+".TIF"
        #open each sample
        pic=Image.open(fileName)
        #crop it accrding to the letter that is being extracted
        if letter==0:
            pic=pic.crop((2000,100,2400,500)).convert("L").rotate(90)
        elif letter==1:
            pic=pic.crop((2000,620,2400,1020)).convert("L").rotate(90)
        elif letter==2:
            pic=pic.crop((2000,1060,2400,1460)).convert("L").rotate(90)
        elif letter==3:
            pic=pic.crop((2000,1600,2400,2000)).convert("L").rotate(90)
        elif letter==4:
            pic=pic.crop((2000,2090,2400,2490)).convert("L").rotate(90)
        elif letter==5:
            pic=pic.crop((2000,2550,2400,2950)).convert("L").rotate(90)
        elif letter==6:
            pic=pic.crop((2000,3020,2400,3420)).convert("L").rotate(90)
        elif letter==7:
            pic=pic.crop((1300,100,1700,500)).convert("L").rotate(90)
        elif letter==8:
            pic=pic.crop((1300,620,1700,1020)).convert("L").rotate(90)
        elif letter==9:
            pic=pic.crop((1300,1060,1700,1460)).convert("L").rotate(90)
        elif letter==10:
            pic=pic.crop((1300,1600,1700,200)).convert("L").rotate(90)
        elif letter==11:
            pic=pic.crop((1300,2090,1700,2490)).convert("L").rotate(90)
        elif letter==12:
            pic=pic.crop((1300,2550,1700,2950)).convert("L").rotate(90)
        elif letter==13:
            pic=pic.crop((1300,3020,1700,3420)).convert("L").rotate(90)
        elif letter==14:
            pic=pic.crop((830,100,1230,500)).convert("L").rotate(90)
        elif letter==15:
            pic=pic.crop((830,620,1230,1020)).convert("L").rotate(90)
        elif letter==16:
            pic=pic.crop((830,1060,1230,1460)).convert("L").rotate(90)
        elif letter==17:
            pic=pic.crop((830,1600,1230,2000)).convert("L").rotate(90)
        elif letter==18:
            pic=pic.crop((830,2090,1230,2490)).convert("L").rotate(90)
        elif letter==19:
            pic=pic.crop((830,2550,1230,2950)).convert("L").rotate(90)
        elif letter==20:
            pic=pic.crop((830,3020,1230,3420)).convert("L").rotate(90)
        elif letter==21:
            pic=pic.crop((250,100,650,500)).convert("L").rotate(90)
        elif letter==22:
            pic=pic.crop((250,620,650,1020)).convert("L").rotate(90)
        elif letter==23:
            pic=pic.crop((250,1060,650,1460)).convert("L").rotate(90)
        elif letter==24:
            pic=pic.crop((250,1600,650,2000)).convert("L").rotate(90)
        elif letter==25:
            pic=pic.crop((250,2090,650,2490)).convert("L").rotate(90)
#        pic.show()
        #save the image
        savingNumber=str(lastSaved+(letter*NumberofSamples+rep))
#        print savingNumber
#        pic.save("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\mysamples\\"+savingNumber+".png")

           
        
        
 
    
