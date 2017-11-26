# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 23:16:13 2017

@author: Laila Elbeheiry
@andrew id: loe
@modification history:
    start           end
    09/11 23:16     10/11 01:34 
    24/11 07:12     24/11 10:09
@desc: The purpose of this code is to take the handwritten samples that I collected from
the students and crop them into letters and save each letter in my samples file
"""
from PIL import Image

#get the number of samples and the number of the last saved sample
NumberofSamples=int(raw_input("number of samples?"))
lastSaved=int(raw_input("last saved?"))  



#loop 26 times (once for each letter)
for letter in range(26):
    #create a loop with the number of repitions to get all samples
    for rep in range(1,NumberofSamples+1):
        if rep<10:
            fileNumber= "1000"+str(rep)
        else:
            fileNumber="100"+str(rep)
        fileName="C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\moresamples\\lowercase\\"+fileNumber+".TIF"
        #open each sample
        pic=Image.open(fileName)
#        pic.show()
#        crop it according to the letter that is being extracted
        if letter==0:
            pic=pic.crop((1940,140,2340,540)).convert("L").rotate(90)
        elif letter==1:
            pic=pic.crop((1980,665,2380,1065)).convert("L").rotate(90)
        elif letter==2:
            pic=pic.crop((1980,1127,2380,1527)).convert("L").rotate(90)
        elif letter==3:
            pic=pic.crop((1950,1600,2350,2000)).convert("L").rotate(90)
        elif letter==4:
            pic=pic.crop((1940,2050,2340,2450)).convert("L").rotate(90)
        elif letter==5:
            pic=pic.crop((1950,2520,2350,2920)).convert("L").rotate(90)
        elif letter==6:
            pic=pic.crop((1940,3020,2340,3420)).convert("L").rotate(90)
        elif letter==7:
            pic=pic.crop((1325,140,1725,540)).convert("L").rotate(90) 
        elif letter==8:
            pic=pic.crop((1339,650,1739,1050)).convert("L").rotate(90)
        elif letter==9:
            pic=pic.crop((1339,1127,1739,1527)).convert("L").rotate(90)
        elif letter==10:
            pic=pic.crop((1339,1600,1739,2000)).convert("L").rotate(90)
        elif letter==11:
            pic=pic.crop((1339,2050,1739,2450)).convert("L").rotate(90)
        elif letter==12:
            pic=pic.crop((1339,2520,1739,2920)).convert("L").rotate(90)
        elif letter==13:
            pic=pic.crop((1339,3020,1739,3420)).convert("L").rotate(90)
        elif letter==14:
            pic=pic.crop((820,140,1220,540)).convert("L").rotate(90)
        elif letter==15:
            pic=pic.crop((820,650,1220,1050)).convert("L").rotate(90)            
        elif letter==16:
            pic=pic.crop((820,1127,1220,1527)).convert("L").rotate(90)                                                          
        elif letter==17:
            pic=pic.crop((820,1600,1220,2000)).convert("L").rotate(90)
        elif letter==18:
            pic=pic.crop((815,2050,1215,2450)).convert("L").rotate(90)
        elif letter==19:
            pic=pic.crop((815,2520,1215,2920)).convert("L").rotate(90)
        elif letter==20:
            pic=pic.crop((795,3020,1195,3420)).convert("L").rotate(90)
        elif letter==21:
            pic=pic.crop((250,120,650,520)).convert("L").rotate(90)
        elif letter==22:
            pic=pic.crop((250,650,650,1050)).convert("L").rotate(90)
        elif letter==23:
            pic=pic.crop((250,1127,650,1527)).convert("L").rotate(90)
        elif letter==24:
            pic=pic.crop((245,1590,645,1990)).convert("L").rotate(90)
        elif letter==25:
            pic=pic.crop((190,2050,590,2450)).convert("L").rotate(90)
#        pic.show()
        #save the image
        savingNumber=str(lastSaved+(letter*NumberofSamples+rep))
#        print savingNumber
        #the directory of the saving file keeps being changed
        pic.save("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\moresamples\uncropped\\"+savingNumber+".png")

           
        
        
 
    
