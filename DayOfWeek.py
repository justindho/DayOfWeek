# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:36:02 2019

@author: Justin
"""

#import datetime
#from PIL import Image, ImageTk
#import subprocess
#import time

import tkinter as tk

class App:
    
    def __init__(self, master):
        #create a frame (aka container) to hold two widgets (buttons) and show it
        frame = tk.Frame(master)
        frame.pack()
        
        #create QUIT button and show
        self.button = tk.Button(
                frame, text='QUIT', fg='red', command=frame.quit
                )
        self.button.pack(side='right')
        
        #create another button and show
        self.say_testing = tk.Button(frame, text='testing123', fg='blue', command=self.say_testing)
        self.say_testing.pack(side='left')
        
    def say_testing(self):
        print('testing123... testing123')

#create a Tk root widget (a window w/ title bar & decoration)
root = tk.Tk()  

app = App(root)

#create a Label widget (child to root); can display text, image, or other icon
#img = tk.PhotoImage(file="C:\Users\Justin\Documents\Coding Programs\DayOfWeek (More Complex)\Monday.jpg")
#label = tk.Label(image=img)
#w = tk.Label(root, image='"C:\Users\Justin\Documents\Coding Programs\DayOfWeek (More Complex)\Monday.jpg"') 

#tell the widget to size itself to fit the text & make itself visible
#label.pack()    

#show the window & create an event loop to handle events from the user 
root.mainloop()

root.destroy()








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