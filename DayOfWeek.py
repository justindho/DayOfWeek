# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 22:11:42 2019

@author: Justin
"""

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
import datetime

#use this class to create instances for M-Su
class GUI:
    def __init__(self):
        #configure the root window
        self.root = tk.Tk()
        self.root.title('Day of Week')
        self.root.configure(background='green')

        #set window size
        self.root_width = self.root.winfo_screenwidth()
        self.root_height = self.root.winfo_screenheight()
        self.root.geometry('{}x{}'.format(self.root_width, self.root_height))
        
        #create all of the main containers
        self.top_frame = tk.Frame(self.root, width=self.root_width, \
                              height=round(self.root_height/4), bg='red')
        self.btm_frame_lh = tk.Frame(self.root, width=self.root_width/2, \
                                     height=round(self.root_height*3/4), \
                                     bg='blue')
        self.btm_frame_rh = tk.Frame(self.root, width=self.root_width/2, \
                                     height=round(self.root_height*3/4), \
                                     bg='pink')
        
        #layout all of the main containers
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.top_frame.grid(row=0, columnspan=2)
        self.btm_frame_lh.grid(row=1, column=0)
        self.btm_frame_rh.grid(row=1, column=1)
        
        #create the widgets for the top frame
        self.time_label = tk.Label(self.top_frame, text='testing', \
                                   font='Times 150 bold')
#        self.time_canvas = tk.Canvas(self.top_frame, width=self.root_width, \
#                                     height=round(self.root_height/4))
#        self.text_canvas = self.time_canvas.create_text(10, 10, anchor='center')
#        self.time_canvas = self.time_canvas.itemconfig(self.text_canvas, text='testing')
        
        #layout the widgets in the top frame
        self.time_label.grid(row=1, sticky='news')
#        self.time_canvas.grid(row=1, sticky='news').
        
        #create the widgets for the bottom lefthand frame
        today = datetime.datetime.today().weekday()
        self.btm_frame_lh_img = ImageTk.PhotoImage(Image.open(days_of_week[today]))
        self.btm_frame_lh_label = tk.Label(self.btm_frame_lh, \
                                           image=self.btm_frame_lh_img)
        
        #layout the widgets in the bottom lefthand frame
        self.btm_frame_lh_label.grid(row=1, column=1, sticky='W')
        
        #create the widgets for the bottom righthand frame
        self.hour = datetime.datetime.now().hour
        self.ampm_img = 'sun.png' if self.hour <12 else 'moon.png'
        self.btm_frame_rh_img = ImageTk.PhotoImage(Image.open(self.ampm_img))
        self.btm_frame_rh_label = tk.Label(self.btm_frame_rh, \
                                           image=self.btm_frame_rh_img)
        
        #layout the widgets in the bottom righthand frame
        self.btm_frame_rh_label.grid(row=1, column=0, sticky='news')
                        
        #continually update the time and the background image
        self.update_image_clock()        
    
    
    #updates background image and clock
    def update_image_clock(self):
        current_day = datetime.datetime.today().weekday()
#        image = Image.open(days_of_week[current_day])
#        image.thumbnail((self.root_width, self.root_height))
#        self.img_day = ImageTk.PhotoImage(image)
        self.btm_frame_lh_img = ImageTk.PhotoImage(Image.open(days_of_week[current_day]))
        self.photo_day = tk.Label(self.root, image=self.btm_frame_lh_img)
        
        #get current time and convert to 12-hour clock
        now = datetime.datetime.now()
        now = now.strftime('%I:%M:%S')
        
        #update widget contents
        self.time_label.configure(text=now)
#        self.time_canvas.itemconfig(self.text_canvas, text=now)
        self.btm_frame_lh_label.configure(image=self.btm_frame_lh_img)
        self.AM_PM()
        
        #continually update screen every 0.001 seconds
        self.root.after(1000, self.update_image_clock)
    
    #provides new image dimensions to fit to full screen
    def image_new_dims(self, image):
        img_width, img_height = image.size
        ratio_width = self.root_width / img_width
        ratio_height = self.root_height / img_height
        scale = int(max(ratio_width, ratio_height))
#        self.img = ImageTk.PhotoImage(Image.open())
        self.img.width = img_width * scale
        self.img.height = img_height * scale
                
    #updates secondary image to sun/moon based on AM/PM
    def AM_PM(self):
        hour = datetime.datetime.now().hour
        if hour < 12:
            #display image of sun
            self.btm_frame_rh_img = ImageTk.PhotoImage(Image.open('sun.png'))
            self.btm_frame_rh_label.configure(image=self.btm_frame_rh_img)
        elif hour >= 12:
            #display image of moon
            self.btm_frame_rh_img = ImageTk.PhotoImage(Image.open('moon.png'))
            self.btm_frame_rh_label.configure(image=self.btm_frame_rh_img)
        
            
#create dictionary mapping  weekday() output to an image            
days_of_week = {0:'Monday.jpg', 1:'Tuesday.jpg', 2:'Wednesday.jpg', \
                3:'Thursday.jpg', 4:'Friday.jpg', 5:'Saturday.jpg', \
                6:'Sunday.jpg'}
app = GUI()
app.root.mainloop()
