# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:40:14 2017

@author: Laila Elbeheiry
@andrew id: loe
@modification history:
    start           end
    17/11 23:40     18/11 03:53 
    21/11 20:29     21/11 23:14
    22/11 19:03     22/11 21:19
    24/11 06:03     24/11 10:32
    24/11 17:53     24/11 21:03
    25/11 10:12     25/11 23:14
    26/11 03:12     26/11 06:05
"""

from tkFileDialog import askopenfilename 
import tkMessageBox
from Tkinter import*
from PIL import Image,ImageTk 
#import myConverter 
import ttk
from tkFileDialog import askdirectory
from skimage import io as io
from skimage import transform as transform
import Segmentation
import random
import os,sys,sqlite3
from tkFileDialog import *
import traceback



#Main window class
class homeGUI():
    def __init__(self, master):
        #this method of choosing a color is adapted from:
        #http://effbot.org/tkinterbook/tkinter-widget-styling.htm
        tk_rgb = "#%02x%02x%02x" % (1, 1, 57)

        master.configure(bg=tk_rgb)
        self.parent=master
        
        self.leftFrame=Frame(self.parent, bg=tk_rgb)
        self.leftFrame.grid(row=0,column=0)
        
        self.rightFrame=Frame(self.parent,bg=tk_rgb)
        self.rightFrame.grid(row=0,column=1, sticky=NW)
        
        self.tk_rgb = "#%02x%02x%02x" % (132, 143, 164)
        #home button links to the home tab
        self.home=Button(self.leftFrame, text="Home", bg=self.tk_rgb, relief=FLAT,width=10, pady=40, font=("MV Boli",20),cursor="hand1", fg="navy", command=self.activateRightFrameHOME, activebackground="yellow")
        self.home.grid(row=0,column=0,pady=2,sticky=NW)
        
        #convert button links to the convert tab
        self.convert=Button(self.leftFrame, text="Convert", bg=self.tk_rgb, relief=FLAT,width=10, pady=40, font=("MV Boli",20),cursor="hand1", fg="navy", command= self.Ask, activebackground="yellow")
        self.convert.grid(row=1,column=0,pady=2,sticky=NW)
        
        
        #settings button links to the settings tab
        self.settings=Button(self.leftFrame, text="Settings", bg=self.tk_rgb, relief=FLAT,width=10, pady=40, font=("MV Boli",20),cursor="hand1",fg="navy",command=self.activateRightFrameSETTINGS,  activebackground="yellow")
        self.settings.grid(row=2,column=0,pady=2,sticky=NW)
        
        #about button links to the about tab
        self.about=Button(self.leftFrame, text="About", bg=self.tk_rgb, relief=FLAT,width=10, pady=40, font=("MV Boli",20),cursor="hand1",fg="navy", command=self.activateRightFrameABOUT,  activebackground="yellow")
        self.about.grid(row=3,column=0,pady=2,sticky=NW)
        
        
        self.activateRightFrameHOME()
        
        #properties of the output file        
        self.outputFormat="txt"
        self.NLD="off"
        self.fname=None
        self.fdirectory=None
        
        #this method determines which button should be highligheted
        self.whatisActive="home"
        
        
    #this function is the commond of the home button
    #it opens the home tab
    def activateRightFrameHOME(self):
        #delete everything in the right frame
        for widget in self.rightFrame.winfo_children():
            widget.destroy()
        #pass the right frame to the home class to add the widgets of the home tab
        home(self.rightFrame)
        self.whatisActive="home"
        #highlight the hume button
        self.activateButton()
        
    #this function opens the convert tab
    def activateRightFrameCONVERT(self):
        #if settings are missing raise an error message
        if self.fname==None or self.fdirectory==None:
            tkMessageBox.showerror("Missing Settings", "cannot convert image until settings are adjusted")
            return
        #if settings are not missing then open the convert tab
        for widget in self.rightFrame.winfo_children():
            widget.destroy()
        convert(self.rightFrame, self)
        self.whatisActive="convert"
        #highilight the convert button
        self.activateButton()

    #this function opens the settings tab
    def activateRightFrameSETTINGS(self):
        for widget in self.rightFrame.winfo_children():
            widget.destroy()        
        settings(self.rightFrame, self)
        self.whatisActive="settings"
        #highlight the settings button
        self.activateButton()
        
    #this function opens the about tab
    def activateRightFrameABOUT(self):
        for widget in self.rightFrame.winfo_children():
            widget.destroy()        
        about(self.rightFrame)
        self.whatisActive="about"
        #highlight about button
        self.activateButton()
        
    #this function is executed when the convert button is clicked
    def Ask(self):
        #if user wants to adjust settings open settings tab
        if not tkMessageBox.askyesno("Convert","Are you sure you want to continue with the current settings?"):
            self.activateRightFrameSETTINGS()
        else:
            #otherwise open the convert tab
            self.activateRightFrameCONVERT()
               
    #this function highlights the butotn that corresponds to the active tab       
    def activateButton(self):
        #find which tab is active 
        #highlight its button in yellow
        #unhighlight other buttons
        if self.whatisActive=="home":
            self.home.config(bg="yellow")
            self.convert.config(bg=self.tk_rgb)
            self.settings.config(bg=self.tk_rgb)
            self.about.config(bg=self.tk_rgb)
        elif self.whatisActive=="convert":
            self.home.config(bg=self.tk_rgb)
            self.convert.config(bg="yellow")
            self.settings.config(bg=self.tk_rgb)
            self.about.config(bg=self.tk_rgb)
        elif self.whatisActive=="settings":
            self.home.config(bg=self.tk_rgb)
            self.convert.config(bg=self.tk_rgb)
            self.settings.config(bg="yellow")
            self.about.config(bg=self.tk_rgb)
        elif self.whatisActive=="about":
            self.home.config(bg=self.tk_rgb)
            self.convert.config(bg=self.tk_rgb)
            self.settings.config(bg=self.tk_rgb)
            self.about.config(bg="yellow")


#this class adds widgets to the right frame of the main window
#if the home tab is opened
class home():
    def __init__(self,f):
        tk_rgb = "#%02x%02x%02x" % (1, 1, 57)
        self.welcome=Label(f,bg=tk_rgb, text="Welcome to EEE-ICR.",font=("MV Boli",30), fg="white", anchor=NW, justify=LEFT)
        self.welcome.grid(row=0,column=0, padx=5, pady=3, sticky=N+W)
        self.explain=Label(f, bg=tk_rgb, text= "EEE-ICR is an extremely, exceptionally, exceedignly intelligent character recognizer =D", font=("MV Boli",10), fg="white", anchor=NW)        
        self.explain.grid(row=1,column=0, padx=5)
        self.summary=Label(f, bg=tk_rgb, text="In order to use the program you need to do three things\nWrite something\nScan it\nChill\n\n\n\nAnd the program will take care of the rest", font=("MV Boli",20), justify=LEFT, anchor=NW, fg="white")
        self.summary.grid(row=2,column=0, padx=5)
        
        
#this class adds widgets to the right frame of the main window
#if the convert tab is opened        
class convert():
    #initialize attributes of this class
    def __init__(self,f, mainClass):
        
        self.mainClass=mainClass
        tk_rgb = "#%02x%02x%02x" % (1, 1, 57)
        self.instructionsTitle=Label(f,bg=tk_rgb, text="Instructions", font=("MV Boli",30), fg="white", anchor=NW)
        self.instructionsTitle.grid(row=0,column=0,padx=10,pady=3, sticky=NW)
        self.instructions=Label(f,bg=tk_rgb, text="Currenlty, EEE-ICR only recognizes English text\n Please make sure that the image is scanned in high quality\n Only lowercase letters are allowed\n EEE-ICR only supports "'jpg'","'jpeg'","'gif'","'TIFF'"\n Once you upload your image, please adjust its orientation\n That's it, simple enough? =D", font=("MV Boli",15), fg="white", anchor=NW)
        self.instructions.grid(row=1,column=0,padx=10,pady=3, sticky=NW)
        self.browse=Button(f,text="browse", padx=5,pady=1, command=self.browseImage)
        self.browse.grid(row=2,column=0)
        self.image=None
        self.im=None
        self.filename=None
        
    #this function is executed when the browse button is clicked 
    #that allows the user to brwose an image
    def browseImage(self):
        self.filename = askopenfilename()
        #if the user clicks cancel then return
        if len(self.filename)<1:
            return
        #check if the extension of the image is allowed
        if self.filename[len(self.filename)-3:]!= "gif"  and self.filename[len(self.filename)-3:]!="jpg" and self.filename[len(self.filename)-3:]!="TIF" and self.filename[len(self.filename)-3:]!="peg" and self.filename[len(self.filename)-3:]!="iff":
            #if it's not then raise an error message
            tkMessageBox.showerror("Error", "Inappropriate format, please review instructions")   
        #if extension is allowed then import the image
        #for the sake of resolution and editting, image is loaded using skimage and PiL and tkimage
        else:
            self.skimage=io.imread(self.filename, as_grey=True)
            #resize an image to fit the canvas
            self.skimage=transform.resize(self.skimage,(500,500))
            io.imsave(self.filename, self.skimage)
            self.pilimage=Image.open(self.filename)  
            self.image=ImageTk.PhotoImage(self.pilimage)

            #open a new window to display the image in it
            t=Toplevel()
            #add widgets from the display image class
            image=displayImage(t,self)
        

#this class adds widgets to the displayed image window
class displayImage():
    #initialize instances
    def __init__(self,master, other):
         self.otherClass=other
         self.master=master
         self.w=Canvas(self.master,width=500,height=500)       
         self.w.pack(fill=BOTH, expand=YES,side=LEFT)
         self.w.create_image(0,0,anchor='nw',image=self.otherClass.image)
         tk_rgb = "#%02x%02x%02x" % (59, 56, 56)
         self.adjustments=Frame(self.master,bg="white",width=50)
         self.adjustments.pack(fill=Y, expand=YES,side=RIGHT, anchor=E)
         
         self.empty=Label(self.adjustments,bg="white")
         self.empty.grid(row=0,column=0,pady=40)
         
         #add rotation buttons
         l=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\icon_images\leftrotate.gif")
         l=l.resize((30,30))
         self.l=ImageTk.PhotoImage(l)
         self.leftRot=Button(self.adjustments,image=self.l, bg="white", command=self.rotatel)
         self.leftRot.image=self.l
         self.leftRot.grid(row=1,column=0)    
         
         l=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\icon_images\\90l.gif")
         l=l.resize((30,30))
         self.L90=ImageTk.PhotoImage(l)
         self.leftRot90=Button(self.adjustments,image=self.L90, bg="white", command=self.rotateL)
         self.leftRot90.image=self.L90
         self.leftRot90.grid(row=2,column=0)         

         l=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\icon_images\\90r.gif")
         l=l.resize((30,30))
         self.R90=ImageTk.PhotoImage(l)
         self.rightRot90=Button(self.adjustments,image=self.R90, bg="white", command=self.rotateR)
         self.rightRot90.image=self.R90
         self.rightRot90.grid(row=3,column=0)       
         
         l=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\icon_images\\rightrotate.gif")
         l=l.resize((30,30))
         self.r=ImageTk.PhotoImage(l)
         self.rightRot=Button(self.adjustments,image=self.r, bg="white", command=self.rotater)
         self.rightRot.image=self.r
         self.rightRot.grid(row=4,column=0)    
         
         #generate a random name so that the orginial image is not overwritten by the editted image
         self.randomName=self.generateRandomName()
        
         io.imsave(self.randomName,self.otherClass.skimage)
         
         done=Button(self.adjustments, text="convert", bg="navy", fg="white", command=self.startSegmenting)
         done.grid(row=5,column=0, pady=20)

    #this function generates a random name to save the editted and rotated image
    def generateRandomName(self):
        #generate a random float between 0 and 1 and append it to the original file name
        name=self.otherClass.filename
        lastIndex=len(name)-1
        while name[lastIndex]!=".":
            name=self.otherClass.filename[:lastIndex]
            lastIndex-=1
        name=name[:lastIndex]+str(random.random())[2:]+self.otherClass.filename[lastIndex:]            
        return name

    #this function rotates an image by .25 degree counterclockwise     
    def rotatel(self):
        #rotate the image using skimage
        self.otherClass.skimage=transform.rotate(self.otherClass.skimage,0.25, mode="edge")
        #save rotated image
        io.imsave(self.randomName,self.otherClass.skimage)
        #display rotated image on canvas
        self.otherClass.pilimage=Image.open(self.randomName)
        self.otherClass.image=ImageTk.PhotoImage(self.otherClass.pilimage)
        self.w.delete("all")
        self.w.create_image(0,0,anchor='nw',image=self.otherClass.image)
    
#this function rotates an image by .25 degrees clockwise    
    def rotater(self):
        #rotate the image using skimage
        self.otherClass.skimage=transform.rotate(self.otherClass.skimage,359.25, mode="edge")
        #save rotated image
        io.imsave(self.randomName,self.otherClass.skimage)
        #display ritate image on canvas
        self.otherClass.pilimage=Image.open(self.randomName)
        self.otherClass.image=ImageTk.PhotoImage(self.otherClass.pilimage)
        self.w.delete("all")
        self.w.create_image(0,0,anchor='nw',image=self.otherClass.image)
        
        
    #similar to rotatel but angle is 90 counterclockwise
    def rotateL(self):
        self.otherClass.skimage=transform.rotate(self.otherClass.skimage,90.0,mode="edge")
        io.imsave(self.randomName,self.otherClass.skimage)
        self.otherClass.pilimage=Image.open(self.randomName)
        self.otherClass.image=ImageTk.PhotoImage(self.otherClass.pilimage)
        self.w.delete("all")
        self.w.create_image(0,0,anchor='nw',image=self.otherClass.image)
        
        
    #similar to rotater but angle is 90 clockwise
    def rotateR(self):
        self.otherClass.skimage=transform.rotate(self.otherClass.skimage,270.0, mode="edge")
        io.imsave(self.randomName,self.otherClass.skimage)
        self.otherClass.pilimage=Image.open(self.randomName)
        self.otherClass.image=ImageTk.PhotoImage(self.otherClass.pilimage)
        self.w.delete("all")
        self.w.create_image(0,0,anchor='nw',image=self.otherClass.image)

    #this function is executed when the convert button is clicked
    def startSegmenting(self):
        #pass the image to the function that converts it into a string
        recognizedText= Segmentation.segPic(self.randomName, self.otherClass.mainClass.NLD)
        fileName=self.otherClass.mainClass.fdirectory+"\\"+self.otherClass.mainClass.fname+"."+self.otherClass.mainClass.outputFormat
        #open a file at the location that the user selected and save the text into it
        #save the file with the name that the user chose
        f=open(fileName,"w")
        f.write(recognizedText)
        f.close()
        
        """  THIS CLASS IS COPIED FROM THE FOLLOWING URL:
        https://github.com/edward344/NotePad/blob/master/notepad.py """
        #THIS IS THE ALGORITHM FOR THE EDITTING WINDOW
        #THE WINDOW IS OPENED AFTER AN IMAGE IS CONVERTED INTO TECT
        class FontStlye(object):
            def __init__(self,app):
                self.top = Toplevel()
                self.top.title("Font Style")
                #---------------------------------------------------------------
                label = Label(self.top,text="Please select a font style...",width=30)
                label.pack()
                #---------------------------------------------------------------
                styles = (
                        "normal",
                        "bold",
                        "italic")
                #---------------------------------------------------------------
                for style in styles:
                    Radiobutton(self.top,text=style,variable=app.style,value=style).pack(anchor=W)
                #---------------------------------------------------------------
                frame = Frame(self.top)
                frame.pack()
                applyButton = Button(frame,text="Apply",command=self.applyfontstyle)
                applyButton.pack(side=LEFT)
                acceptButton = Button(frame,text="Accept",command=self.applyfontstyle_exit)
                acceptButton.pack(side=RIGHT)
                #---------------------------------------------------------------
                self.app = app
                
            def applyfontstyle(self):
                self.app.fontstyle = self.app.style.get()
                self.app.text.config(font=(self.app.font,self.app.fontsize,self.app.fontstyle))
                
            def applyfontstyle_exit(self):
                self.app.fontstyle = self.app.style.get()
                self.app.text.config(font=(self.app.font,self.app.fontsize,self.app.fontstyle))
                self.top.destroy()
        #=======================================================================
        class FontType(object):
            def __init__(self,app):
                self.top = Toplevel()
                self.top.title("Font")
                #---------------------------------------------------------------
                label = Label(self.top,text="Please select a font...",width=30)
                label.pack()
                #---------------------------------------------------------------
                fonts = (
                        "Arial",
                        "Courier New",
                        "Verdana",
                        "Times New Roman",
                        "Comic Sans MS",
                        "Fixedsys",
                        "MS Sans Serif",
                        "MS Serif",
                        "Symbol",
                        "System")
                #---------------------------------------------------------------
                for font in fonts:
                    Radiobutton(self.top,text=font,variable=app.fontvar,value=font).pack(anchor=W)
                #---------------------------------------------------------------
                frame = Frame(self.top)
                frame.pack()
                applyButton = Button(frame,text="Apply",command=self.applyfont)
                applyButton.pack(side=LEFT)
                acceptButton = Button(frame,text="Accept",command=self.applyfont_exit)
                acceptButton.pack(side=RIGHT)
                #---------------------------------------------------------------
                self.app = app
                
            def applyfont(self):
                self.app.font = self.app.fontvar.get()
                self.app.text.config(font=(self.app.font,self.app.fontsize,self.app.fontstyle))
                
            def applyfont_exit(self):
                self.app.font = self.app.fontvar.get()
                self.app.text.config(font=(self.app.font,self.app.fontsize,self.app.fontstyle))
                self.top.destroy()
        #=======================================================================
        class FontSize(object):
            def __init__(self,app):
                self.top = Toplevel()
                self.top.title("Font Size")
                #---------------------------------------------------------------
                label = Label(self.top,text="Please select a font size...",width=30)
                label.pack()
                #---------------------------------------------------------------
                self.scale = Scale(self.top,from_=10,to=25,orient=HORIZONTAL)
                self.scale.pack()
                self.scale.set(app.fontsize)
                #---------------------------------------------------------------
                frame = Frame(self.top)
                frame.pack()
                applyButton = Button(frame,text="Apply",command=self.applyfontsize)
                applyButton.pack(side=LEFT)
                acceptButton = Button(frame,text="Accept",command=self.applyfontsize_exit)
                acceptButton.pack(side=RIGHT)
                #---------------------------------------------------------------
                self.app = app
                
            def applyfontsize(self):
                self.app.fontsize = self.scale.get() 
                self.app.text.config(font=(self.app.font,self.app.fontsize,self.app.fontstyle))
            
            def applyfontsize_exit(self):
                self.app.fontsize = self.scale.get() 
                self.app.text.config(font=(self.app.font,self.app.fontsize,self.app.fontstyle))
                self.top.destroy()
        #=======================================================================
        #++++++++++++++++++++Main Class+++++++++++++++++++++++++++++++++++++++++
        class App(object):
            file_name = "Untitled"
            changed = False
            fontsize = 12 #Hold the font size;
            font = "Courier New" #Hold the font;
            fontstyle = "normal" #hold the font style;
            def __init__(self,master):
                self.master = master
                master.title("Untitled: NotePad")
                master.geometry("640x480")
                
                #--Execute SQLite to retrieve the previous font, fontsize and fontstyle:
                self.retrieve_data()
                #---------------------------------------------------------------
                # add a menu: ..................................................
                menubar = Menu(master)
                filemenu = Menu(menubar,tearoff=0)
                filemenu.add_command(label="New",command=self.new_file)
                filemenu.add_command(label="Open",command=self.open_file)
                filemenu.add_command(label="Save",command=self.save_file)
                filemenu.add_command(label="Save as",command=self.save_as_file)
                filemenu.add_command(label="Exit",command=self.exit_menu)
                menubar.add_cascade(label="File",menu=filemenu)
                #---------------------------------------------------------------
                editmenu = Menu(menubar,tearoff=0)
                editmenu.add_command(label="Cut",command=self.cut)
                editmenu.add_command(label="Copy",command=self.copy)
                editmenu.add_command(label="Paste",command=self.paste)
                menubar.add_cascade(label="Edit",menu=editmenu)
                #---------------------------------------------------------------
                optionmenu = Menu(menubar,tearoff=0)
                optionmenu.add_command(label="Font",command=self.changefont)
                optionmenu.add_command(label="Font Size",command=self.changefontsize)
                optionmenu.add_command(label="Font Style",command=self.changefontstyle)
                menubar.add_cascade(label="Options",menu=optionmenu)
                #---------------------------------------------------------------
                master.config(menu=menubar)
                #---------------------------------------------------------------
                scrollbar = Scrollbar(master)
                scrollbar.pack(side=RIGHT,fill=Y)
                #---------------------------------------------------------------
                self.text = Text(master,yscrollcommand=scrollbar.set)
                #ADDING THE RECOGNIZED TEXT
                self.text.insert(END,recognizedText)
                self.text.bind("<Button-3>",self.popmenu)
                self.text.pack(side=LEFT,fill=BOTH,expand=1)
                scrollbar.config(command=self.text.yview)
                #---------------------------------------------------------------
                self.text.bind("<Key>",self.key_callback)
                #~ self.text.bind("<Return>",self.return_key)
                #---------------------------------------------------------------
                master.protocol("WM_DELETE_WINDOW",self.close_window)
                #---------------------------------------------------------------
                #...............................................................
                if len(sys.argv) > 1:
                    if sys.platform == "win32":
                        if sys.argv[1][-4:] == ".txt":
                            try:
                                f = open(sys.argv[1])
                                for line in f:
                                    self.text.insert(END,line)
                                f.close()
                                self.file_name = sys.argv[1]
                                self.master.title(self.file_name[self.file_name.rfind("/")+1:] + ": NotePad")
                                self.changed = False
                            except IOError:
                                tkMessageBox.showwarning("Open file","Cannot open this file...")
                    else:
                        try:
                            f = open(sys.argv[1])
                            for line in f:
                                self.text.insert(END,line)
                            f.close()
                            self.file_name = sys.argv[1]
                            self.master.title(self.file_name[self.file_name.rfind("/")+1:] + ": NotePad")
                            self.changed = False
                        except IOError:
                            tkMessageBox.showwarning("Open file","Cannot open this file...")
                #---------------------------------------------------------------
                self.fontvar = StringVar() #hold the variable for radiobutton.
                self.fontvar.set(self.font)
                #---------------------------------------------------------------
                self.style = StringVar() #Hold the style variable for radiobutton
                self.style.set(self.fontstyle)
                # Set the font, font size and font style: ----------------------
                self.text.config(font=(self.font,self.fontsize,self.fontstyle))
        
        	#===================================================================
        	
            # Retrieve data from a database: -----------------------------------
            def retrieve_data(self):
                try:
                    connection = sqlite3.connect("config.db")
                    cursor = connection.cursor()    
        
                    cursor.execute("SELECT font FROM info")
                    self.font = str(cursor.fetchone()[0])
                    
                    cursor.execute("SELECT size FROM info")
                    self.fontsize = cursor.fetchone()[0]
                    
                    cursor.execute("SELECT style FROM info")
                    self.fontstyle = str(cursor.fetchone()[0])
                    
                    connection.close()
                except sqlite3.OperationalError:
                    #if the database does not exist we create a new one:
                    connection = sqlite3.connect("config.db")
                    cursor = connection.cursor()
                    cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS info (id INTEGER PRIMARY KEY NOT NULL,
                                    font TEXT NOT NULL, size INTEGER NOT NULL,style TEXT NOT NULL)
                                    """)
                            
                    #connection.commit()
                    cursor.execute("""
                                    INSERT INTO info VALUES (1,'Courier New',12,'normal')
                                    """)
                    connection.commit()
                    connection.close()
                
            # Update data to the database: -------------------------------------
            def update_data(self):
                # Store the font, fontsize and fontstyle in a database:
                commit = False
                connection = sqlite3.connect("config.db")
                cursor = connection.cursor()
                    
                cursor.execute("SELECT font FROM info")
                if self.font != str(cursor.fetchone()[0]):
                    cursor.execute("UPDATE info SET font = ? WHERE id = 1",(self.font,))
                    commit = True
                        
                cursor.execute("SELECT size FROM info")
                if self.fontsize != cursor.fetchone()[0]:
                    cursor.execute("UPDATE info SET size = ? WHERE id = 1",(self.fontsize,))
                    commit = True
                    
                cursor.execute("SELECT style FROM info")
                if self.fontsize != str(cursor.fetchone()[0]):
                    cursor.execute("UPDATE info SET style = ? WHERE id = 1",(self.fontstyle,))
                    commit = True
                    
                if commit:
                    connection.commit()
                connection.close()
                
            # Option Menu ------------------------------------------------------
            def changefontsize(self):
                obj = FontSize(self)
                
            def changefont(self):
                obj = FontType(self)
                
            def changefontstyle(self):
                obj = FontStlye(self)
            #...................................................................
            def open_file(self):
                filename = str(askopenfilename(title="Open File",filetypes=[('text file','.txt')]))
                if len(filename) > 0:
                    self.text.delete("1.0",END)
                    try:
                        f = open(filename)
                        for line in f:
                            self.text.insert(END,line)
                        f.close()
                        self.file_name = filename
                        self.master.title(filename[filename.rfind("/")+1:] + ": NotePad")
                        self.changed = False
                    except IOError:
                        tkMessageBox.showwarning("Open file","Cannot open this file...") 
                        
            def save_file(self):
                if self.file_name == "Untitled":
                    self.save_as_file()
                else:
                    f = open(self.file_name,"w")
                    text = self.text.get("1.0",END).encode("utf-8")
                    f.write(text)
                    f.close()
                    self.changed = False   
                    self.master.title(self.file_name[self.file_name.rfind("/")+1:] + ": NotePad")
            
            def save_as_file(self):
                filename = str(asksaveasfilename(title="Save as File",defaultextension=".txt",filetypes=[('text file','.txt')]))
                if len(filename) > 0:
                    f = open(filename,"w")
                    text = self.text.get("1.0",END).encode("utf-8")
                    f.write(text)
                    f.close()
                    self.file_name = filename
                    self.master.title(filename[filename.rfind("/")+1:] + ": NotePad")
                    self.changed = False
                
            def close_window(self):
                self.update_data()
                if self.changed:
                    if tkMessageBox.askyesno("Quit","do you want to save the file..."):
                        if self.file_name == "Untitled":
                            self.save_as_file()
                        else:
                            f = open(self.file_name,"w")
                            text = self.text.get("1.0",END).encode("utf-8")
                            f.write(text)
                            f.close()
                            self.master.destroy()
                    else:
                        self.master.destroy()
                else:
                    self.master.destroy()
                
            def key_callback(self,event):
                if not self.changed:
                    self.master.title("*" + self.file_name[self.file_name.rfind("/")+1:] + ": NotePad")
                    self.changed = True
                
            def popmenu(self,event):
                menu = Menu(self.master,tearoff=0)
                menu.add_command(label="Cut",command=self.cut)
                menu.add_command(label="Copy",command=self.copy)
                menu.add_command(label="Paste",command=self.paste)
                menu.post(event.x_root,event.y_root)
        
                
            def cut(self):
                try:
                    self.copy()
                    self.text.delete("sel.first","sel.last")
                    self.master.title("*" + self.file_name[self.file_name.rfind("/")+1:] + ": NotePad")
                    self.changed = True
                except TclError:
                    pass
                
            def copy(self):
                try:
                    self.text.clipboard_clear()
                    text = self.text.get("sel.first","sel.last")
                    self.text.clipboard_append(text)
                    
                except TclError:
                    pass
                        
            def paste(self):
                try:
                    text = self.text.selection_get(selection="CLIPBOARD")
                    self.text.insert(INSERT,text)
                    self.master.title("*" + self.file_name[self.file_name.rfind("/")+1:] + ": NotePad")
                    self.changed = True
                except TclError:
                    pass
                    
            #----------File menu commands:--------------------------------------
                
            def open_file_menu(self):
                if self.changed:
                    if tkMessageBox.askyesno("Quit","do you want to save the file..."):
                        if self.file_name == "Untitled":
                            obj = Save_File(self,"Save as")
                        else:
                            f = open(self.file_name,"w")
                            text = self.text.get("1.0",END).encode("utf-8")
                            f.write(text)
                            f.close()
                            #---------------------------------------------------
                    self.text.delete("1.0",END)
                    self.file_name = "Untitled"
                    self.master.title("Untitled: NotePad")
                    self.changed = False
                obj = Open_File(self,"Open")
        
            def save_as_file_menu(self):
                obj = Save_File(self,"Save")
        
           #--------------------------------------------------------------------     
                
            def save_file_menu(self):
                if self.file_name == "Untitled":
                    obj = Save_File(self,"Save as")
                else:
                    f = open(self.file_name,"w")
                    text = self.text.get("1.0",END).encode("utf-8")
                    f.write(text)
                    f.close()
                    self.changed = False
                    self.master.title(self.file_name[self.file_name.rfind("/")+1:] + ": NotePad")
        
            def new_file(self):
                if self.changed:
                    if tkMessageBox.askyesno("New","Do you want to save the file..."):
                        if self.file_name == "Untitled":
                            obj = Save_File(self,"Save as")
                        else:
                            f = open(self.file_name,"w")
                            text = self.text.get("1.0",END).encode("utf-8")
                            f.write(text)
                            f.close()
                self.text.delete("1.0",END)
                self.file_name = "Untitled"
                self.master.title("Untitled: NotePad")
                self.changed = False
                
            def exit_menu(self):
                self.update_data()
                if self.changed:
                    if tkMessageBox.askyesno("Quit","do you want to save the file..."):
                        if self.file_name == "Untitled":
                            self.save_as_file()
                        else:
                            f = open(self.file_name,"w")
                            text = self.text.get("1.0",END).encode("utf-8")
                            f.write(text)
                            f.close()
                            self.master.destroy()
                    else:
                        self.master.destroy()
                else:
                    self.master.destroy()
        #=======================================================================
        
        def main():
            root = Tk()
            app = App(root)
            root.mainloop()
        
        if __name__ == '__main__':
            main()            
            
                    
#this class adds widgets to the right frame of the main window
#if the settings tab is opened
class settings():
    def __init__(self,f,mainClass):
        
        tk_rgb = "#%02x%02x%02x" % (1, 1, 57)
        self.Intro=Label(f, bg=tk_rgb, text="Select your settings:",font=("MV Boli",20), fg="white" )
        self.Intro.grid(row=0, column=0, sticky=W, pady=7)
        
        self.outputLabel=Label(f, bg=tk_rgb,text= "Output File Type:", font=("MV Boli",15), fg="white" )
        self.outputLabel.grid(row=1,column=0, sticky=W, padx=2)
        
        self.variable = StringVar(f)
        self.variable.set("txt") # default value

        self.w = OptionMenu(f, self.variable, "txt")
        self.w.grid(row=1, column=1, sticky=W)
        
        
        #THE CODE FOR THE SEPARATOR IS COPIED FROM THE FOLLOWIING URL:
        #https://stackoverflow.com/questions/38396900/python-tkinter-ttk-separator-with-label
        ttk.Separator(f, orient='horizontal').grid(column=0,row=2, columnspan=3, sticky='EW', pady=7)
        
        self.newLines=Label(f, bg=tk_rgb,text= "New Line Detections:", font=("MV Boli",15), fg="white" )
        self.newLines.grid(row=3,column=0, sticky=W, padx=2)
        
        self.variable1 = StringVar(f)
        self.variable1.set("off") # default value
        self.x = OptionMenu(f, self.variable1, "off", "on")
        self.x.grid(row=3, column=1, sticky=W)
        
        what=Image.open("C:\Users\Beheiry\Desktop\laila\CMU\SEMESTER 1\PROGRAMMING\project\icon_images\whatisthis.jpg")
        what=what.resize((15,15))
        self.what=ImageTk.PhotoImage(what)
        self.whatIsThis=Button(f,image=self.what, bg="white", command=self.explain)
        self.whatIsThis.image=self.what
        self.whatIsThis.grid(row=3,column=2, padx=5)    

        ttk.Separator(f, orient='horizontal').grid(column=0,row=4, columnspan=3, sticky='EW', pady=7)
        
        self.fileNameLabel=Label(f, bg=tk_rgb,text= "Output File Name:", font=("MV Boli",15), fg="white" )
        self.fileNameLabel.grid(row=5,column=0, sticky=W, padx=2)
        self.fileName=Entry(f)
        self.fileName.grid(row=5, column=1, sticky=E)
        self.whatIsThis1=Button(f, image=self.what, bg="white", command=self.explain1)
        self.whatIsThis1.image=self.what
        self.whatIsThis1.grid(row=5,column=2,sticky=E)
        
        ttk.Separator(f, orient='horizontal').grid(column=0,row=6, columnspan=3, sticky='EW', pady=7)
        
        fileLocationLabel=Label(f, bg=tk_rgb,text= "Output File Location:", font=("MV Boli",15), fg="white" )
        fileLocationLabel.grid(row=7, column=0, sticky=W, padx=2)
        
        browseFileLocation = Button(f,text="browse", padx=5,pady=1, command=self.browseImage)
        browseFileLocation.grid(row=7, column=1)
        
        
        self.convertButton=Button(f, text="convert", bg="navy", fg="white", width=8, height=1,font=("MV Boli",20), command= self.Convert)
        self.convertButton.grid(row=8, column=0, columnspan=2, pady=30)
        self.mainClass=mainClass
        
        

    #this function explains what New Line Detections mean
    def  explain(self):
        tkMessageBox.showinfo("New Line Detections", "If you choose off, the program will not consider the lines in your scanned image as separate lines. If you choose on, each line will be considered as separate lines (i.e output will have as many lines as input)")
    
    #this function raises a warning abou the file name
    def  explain1(self):
        tkMessageBox.showinfo("file name", "If file name already exists in the same location, file will be overwritten")
        
     #this function allows the user to choose the location of the output file  
    def browseImage(self):
        self.mainClass.fdirectory=askdirectory()
        
    #this function opens the convert tab
    #and saves the settings as instances of the main class
    def Convert(self):
        #get the variables that were chosen from the listbox
        self.mainClass.NLD=self.variable1.get()
        self.mainClass.outputFormat=self.variable.get()
        #check whether user chosen a file name and a file location or not
        if self.mainClass.fdirectory:
            if self.fileName.get():
                name=self.fileName.get()
                self.mainClass.fname=name
                self.mainClass.activateRightFrameCONVERT()
            else:
                tkMessageBox.showerror("Missing Settings", "please enter file name")            
        else:
            tkMessageBox.showerror("Missing Settings", "please choose file location") 



#this class adds widgets to the right frame of the main window
#if the about tab is opened
class about():
    def __init__(self,f):
        
        tk_rgb = "#%02x%02x%02x" % (1, 1, 57)
        self.one=Label(f,bg=tk_rgb, text="About EEE-ICR",font=("MV Boli",40), fg="white", anchor=W)
        self.one.grid(row=0,column=0, padx=5, pady=3, sticky=W)
        self.two=Label(f,bg=tk_rgb, text="EEE-ICR is a user-friendly program that\nrecognizes and converts handwritten text into digital data.\nPlease read carefully the instructions before using the program.\nThe software is currently limited to English non-cursive text.\nIf you have any inquiries you can contact the developer at:\nloe@andrew.cmu.edu\nor website: https://web2.qatar.cmu.edu/~loe/ ",font=("MV Boli",22), fg="white", anchor=W, justify=LEFT, cursor='xterm')
        self.two.grid(row=1, column=0, padx=5, pady=2, sticky=W)

        
       
wnd=Tk()
firstWindow=homeGUI(wnd)
wnd.mainloop()
