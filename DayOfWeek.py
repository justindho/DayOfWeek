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

#use this class to create instances for M-Su
class Day:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(background='white')
        self.root.geometry("1000x1000")
        self.label = tk.Label(text='')
        self.label.pack()
        self.update_clock()
        self.root.mainloop()
    
    #updates time in window    
    def update_clock(self):
        now = time.strftime('%H:%M:%S')
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)
            
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
        
        panel = tk.Label(self, image=img)
        panel.image = img
        panel.pack(side='bottom', fill='both', expand='yes')
        self.root.after(1000, self.root.mainloop())

#create a Tk root widget (a window w/ title bar & decoration)
#root = tk.Tk()  

app = Day()

#continually update background image based on day of week
while True:
    current_day = datetime.datetime.today().weekday()
    app.update_background_image(current_day)

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








#def kill():
#    try:
#        subprocess.run(['taskkill', '/f', '/im', "dllhost.exe"])
##        'ERROR: The process "dllhost.exe" not found.'
#    except:
#        pass
#
#def dispImage(current_day):
#        if current_day == 0:
#            kill()
#            image = Image.open('Monday.jpg')
#            image.show()
#        elif current_day == 1:
#            kill()
#            image = Image.open('Tuesday.jpg')
#            image.show()
#        elif current_day == 2:
#            kill()
#            image = Image.open('Wednesday.jpg')
#            image.show()
#        elif current_day == 3:
#            kill()
#            image = Image.open('Thursday.jpg')
#            image.show()
#        elif current_day == 4:
#            kill()
#            image = Image.open('Friday.jpg')
#            image.show()
#        elif current_day == 5:
#            kill()
#            image = Image.open('Saturday.jpg')
#            image.show()
#        elif current_day == 6:
#            kill()
#            image = Image.open('Sunday.jpg')
#            image.show()
#    
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