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
from random import randint

#displays image associated with the day of week
#def update_background_image(current_day):
#    if current_day == 0:
#        img = ImageTk.PhotoImage(Image.open('Monday.jpg'))
#    elif current_day == 1:
#        img = ImageTk.PhotoImage(Image.open('Tuesday.jpg'))
#    elif current_day == 2:
#        img = ImageTk.PhotoImage(Image.open('Wednesday.jpg'))
#    elif current_day == 3:
#        img = ImageTk.PhotoImage(Image.open('Thursday.jpg'))
#    elif current_day == 4:
#        img = ImageTk.PhotoImage(Image.open('Friday.jpg'))
#    elif current_day == 5:
#        img = ImageTk.PhotoImage(Image.open('Saturday.jpg'))
#    elif current_day == 6:
#        img = ImageTk.PhotoImage(Image.open('Sunday.jpg'))
#    
#    return img

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
#        self.label = tk.Label(self.frame, image=self.img, text='', \
#                         font='Times 200 bold', compound=tk.CENTER)
        self.label = tk.Label(self.frame, image=self.img, text='', \
                         font='Times 200 bold', compound=tk.CENTER)
        
        self.label.pack()
        
        self.update_image()        
#        self.update_clock()
#        self.root.mainloop()
    
    #updates time in window    
    def update_clock(self):
        now = time.strftime('%H:%M:%S')
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)
    
    #updates background image
    def update_image(self):
#        current_day = datetime.datetime.today().weekday()
        current_day = randint(0,6)  #use for testing purposes
        self.img = ImageTk.PhotoImage(Image.open(days_of_week[current_day]))
        self.photo = tk.Label(self.root, image=self.img)
        self.photo.image = self.img
        self.label.configure(image=self.img)
#        self.label = tk.Label(self.frame, image=self.img, text=time.strftime('%H:%M:%S'), \
#                         font='Times 200 bold', compound=tk.CENTER)
        self.root.after(979, self.update_image)
    
    #resizes image to fit window
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
#        self.img
            
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