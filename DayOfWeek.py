# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:36:02 2019

@author: Justin Ho
"""

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
#from random import randint

#use this class to create instances for M-Su
class GUI:
    def __init__(self):
        #configure the root window
        self.root = tk.Tk()
        self.root.title('Day of Week')
        self.root.configure(background='black')

        #set window size
        self.root_width = self.root.winfo_screenwidth()
        self.root_height = self.root.winfo_screenheight()
        self.root.geometry('{}x{}'.format(self.root_width, self.root_height))
            
        #create child frame to root
        self.frame = tk.Frame(self.root, width=self.root_width, height=self.root_height)
        self.frame.pack()
        
        #open default image
        current_day = datetime.datetime.today().weekday()
        self.img = ImageTk.PhotoImage(Image.open(days_of_week[current_day]))
        
        #save a reference to the image object to prevent garbage-collection
        self.photo = tk.Label(self.root, image=self.img)
        self.photo.image = self.img
        
        #expand assigns addt'l space to the frame if parent is expanded
        self.frame.pack(expand='True')   
        
        #create child label of frame to display text over image
        self.label = tk.Label(self.frame, image=self.img, text='', \
                         font='Times 200 bold', compound=tk.CENTER)
        self.label.pack()
        
        #continually update the time and the background image
        self.update_image_clock()        
#        self.update_clock()
#        self.root.mainloop()
    
    #updates time in window    
#    def update_clock(self):
#        now = time.strftime('%H:%M:%S')
#        self.label.configure(text=now)
#        self.root.after(1000, self.update_clock)
    
    #updates background image and clock
    def update_image_clock(self):
        current_day = datetime.datetime.today().weekday()
#        current_day = randint(0,6)  #use for testing purposes
        self.img = ImageTk.PhotoImage(Image.open(days_of_week[current_day]))
        self.photo = tk.Label(self.root, image=self.img)
#        self.photo.image = self.img
        now = time.strftime('%H:%M:%S')
        self.label.configure(image=self.img, text=now)
#        self.label = tk.Label(self.frame, image=self.img, text=time.strftime('%H:%M:%S'), \
#                         font='Times 200 bold', compound=tk.CENTER)
        self.root.after(1000, self.update_image_clock)
    
    #resizes image to fit window
    def resize_image(self, image):
#        ratio_width = self.root_width / 
#        ratio_height = self.root_height / 
        pass
        
    #updates secondary image to sun/moon based on AM/PM
    def AM_PM(self):
        now = int(time.strftime('%H'))
        if now < 12:
            #display image of sun
            pass
        elif now >= 12:
            #display image of moon
            pass
        pass
            
days_of_week = {0:'Monday.jpg', 1:'Tuesday.jpg', 2:'Wednesday.jpg', \
                        3:'Thursday.jpg', 4:'Friday.jpg', 5:'Saturday.jpg', \
                        6:'Sunday.jpg'}
app = GUI()
app.root.mainloop()

#continually update background image based on day of week
#while True:
#    current_day = datetime.datetime.today().weekday()
#    app.img = update_background_image(current_day)



 
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