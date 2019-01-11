# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:36:02 2019

@author: Justin
"""

#import datetime
#from PIL import Image, ImageTk
#import subprocess
#import time

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    #for Python3
    import tkinter as tk

from PIL import Image, ImageTk
import time
import datetime
#import os


#use this class to create instances for M-Su
class GUI:
    def __init__(self):
        #configure the root window
        self.root = tk.Tk()
        self.root.title('Day of Week')
#        self.root.configure(background='white')

        #set window size
#        w = '2000'
#        h = '2000'
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry('{}x{}'.format(w, h))
        
        
        #create child frame to root
        self.frame = tk.Frame(self.root) 
        
        #open default image
        self.img = ImageTk.PhotoImage(Image.open('Monday.jpg')) 
        
        #expand assigns addt'l space to the frame if parent is expanded
        self.frame.pack(expand='True')   
        
        #create child label of frame to display text over image
        self.label = tk.Label(self.frame, image=self.img, text='testing', \
                         font='Times 200 bold', compound=tk.CENTER)
        
#        self.label = tk.Label(text='')
        self.label.pack()
        
        self.update_clock()
#        self.root.mainloop()
    
    #updates time in window    
    def update_clock(self):
        now = time.strftime('%H:%M:%S')
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)
    
    #resizes image to fit window
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
#        self.img
            
#displays image associated with the day of week
def update_background_image(self, current_day):
    if current_day == 0:
        img = ImageTk.PhotoImage(Image.open('Monday.jpg'))
    elif current_day == 1:
        img = ImageTk.PhotoImage(Image.open('Tuesday.jpg'))
    elif current_day == 2:
        img = ImageTk.PhotoImage(Image.open('Wednesday.jpg'))
    elif current_day == 3:
        img = ImageTk.PhotoImage(Image.open('Thursday.jpg'))
    elif current_day == 4:
        img = ImageTk.PhotoImage(Image.open('Friday.jpg'))
    elif current_day == 5:
        img = ImageTk.PhotoImage(Image.open('Saturday.jpg'))
    elif current_day == 6:
        img = ImageTk.PhotoImage(Image.open('Sunday.jpg'))
    
#        label = tk.Label(image=photo)
#        label.image = photo    #keep a reference
#        label.pack()
    
#        w = img.width()
#        h = img.height()
#        self.geometry("%dx%d+0+0" % (w, h))
    
    self.label = tk.Label(self, image=img)
    self.label.image = img
    self.panel.pack(side='bottom', fill='both', expand='yes')
    self.root.after(1000, self.root.mainloop())


app = GUI()
app.root.mainloop()

#continually update background image based on day of week
#while True:
#    current_day = datetime.datetime.today().weekday()
#    update_background_image(current_day)

#create a Tk root widget (a window w/ title bar & decoration)
#root = tk.Tk()
#root.title('Day of Week')
#
#label = tk.Label(root)
#img = ImageTk.PhotoImage(Image.open('Monday.jpg'))
#
#width = root.winfo_screenwidth()
#height = root.winfo_screenheight()
#root.geometry(("%dx%d")%(width, height))
##dimensions = "image size: %dx%d" % (img.width(), img.height())
#label = tk.Label(image=img)
#label.image = img
#label.pack(side='bottom', fill='both', expand='yes')


#show the window & create an event loop to handle events from the user 
#root.mainloop()

#root.destroy()




 
#while True:
#    current_hour = datetime.datetime.today().hour
#    current_day = datetime.datetime.today().weekday()
#    if current_hour == 0:
#        dispImage(current_day)
#        time.sleep(82800)   #wait 23 hours to check the time again
#    else:
#        dispImage(current_day)
#        time.sleep((24 - current_hour) * 3600)  #wait til midnight to check the day again
#
#input("Press enter to close program")