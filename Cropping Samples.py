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
        fileNumber=str(10008+rep)
        fileName="C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\moresamples\\2017-11-11\\"+fileNumber+".TIF"
        #open each sample
        pic=Image.open(fileName)
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
        if letter>16:
            pic.show()
#        pic.show()
        #save the image
        savingNumber=str(lastSaved+(letter*NumberofSamples+rep))
#        print savingNumber
#        pic.save("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\mysamples\\"+savingNumber+".png")

           
        
        
 
    
