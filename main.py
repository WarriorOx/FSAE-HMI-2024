import customtkinter as ctk
from tkinter import *
import math
import random
import time

#parameters
width = 1024
height = 600
dial_rad = int(0.5*(width/2)) #dial radius
center = [width/2,height/2]
needle = [0.85, 0.3]
min_speed = 0
max_speed = 200 #kph
step_speed = 20 #smallest gradations of the meter that have text labels IE. 20, 40, etc.
min_rpm = 0
max_rpm = 10000
step_rpm = 1000

#startup
root = ctk.CTk()
root.wm_attributes('-fullscreen', True)
ctk.set_appearance_mode("Dark")
meter_font = ctk.CTkFont(family="Source Sans Pro Light", size=12, weight="normal")
#root.geometry(f"{width}x{height}")

#set titles
def setTitles():
    root.title('DisplayTest')
    speed.itemconfig(speed.title,text="Speed")
    speed.itemconfig(speed.unit,text="KM/H")
    rpm.itemconfig(rpm.title,text="RPM")
    rpm.itemconfig(rpm.unit,text="RPM")

class Speedometer(Canvas):
    
    x0 = center[0]
    y0 = center[1]

    def draw(self, vmin, vmax, v_step, title, unit):
        self.vmin = vmin
        self.vmax = vmax
        #dial_rad = int(0.5*(width/2)) #Do I need this?
        self.title = self.create_text(width/2, 12, fill="#03004f", font=meter_font) #Window background
        self.create_oval(self.x0-dial_rad*1.1, self.y0-dial_rad*1.1, self.x0+dial_rad*1.1, self.y0+dial_rad*1.1, fill="grey")# grey outer ring
        self.create_oval(self.x0-dial_rad, self.y0-dial_rad, self.x0+dial_rad, self.y0+dial_rad, fill="#03004f") #Dial background
        self.create_oval(self.x0-dial_rad*0.1, self.y0-dial_rad*0.1, self.x0+dial_rad*0.1, self.y0+dial_rad*0.1, fill="#e3b322") #Connection point of the needle

        #Loop to fill gradations of the dial
        for i in range(1+int((vmax-vmin)/v_step)):
            v = vmin + v_step * i
            angle = (5+6*((v-vmin)/(vmax-vmin)))*math.pi/4
            self.create_line(self.x0+dial_rad*math.sin(angle)*0.9,
                             self.y0-dial_rad*math.cos(angle)*0.9,
                             self.x0+dial_rad*math.sin(angle)*0.98,
                             self.y0-dial_rad*math.cos(angle)*0.98,
                             fill = "#e3b322")#,font=meter_font)
            if i == int(vmax-vmin)/v_step:
                continue
            for dv in range(1,5):
                angle = (5+6*((v+dv*(v_step/5)-vmin)/(vmax-vmin)))*math.pi/4
                self.create_line(self.x0+dial_rad*math.sin(angle)*0.94,
                    self.y0-dial_rad*math.cos(angle)*0.94,
                    self.x0+dial_rad*math.sin(angle)*0.98,
                    self.y0-dial_rad*math.cos(angle)*0.98,fill="#e3b322")
        self.unit = self.create_text(width/2,self.y0+0.8*dial_rad,fill="#e3b322", font=meter_font)
        self.needle = self.create_line(self.x0-dial_rad*math.sin(5*math.pi/4)*needle[1],
            self.y0+dial_rad*math.cos(5*math.pi/4)*needle[1],
            self.x0+dial_rad*math.sin(5*math.pi/4)*needle[0],
            self.y0-dial_rad*math.cos(5*math.pi/4)*needle[0],
            width=2,fill="#e3b322")
        lb1=Label(self, compound='right', textvariable=v)
    
    #Draws the needle based on input data
    def draw_needle(self, v):
        v = max(v, self.vmin) #if v is less than min stays at min
        v = min(v, self.vmax)# if v is more than max stays at max
        angle = (5+6*((v-self.vmin)/(self.vmax-self.vmin)))*math.pi/4
        self.coords(self.needle,self.x0-dial_rad*math.sin(angle)*needle[1],
            self.y0+dial_rad*math.cos(angle)*needle[1],
            self.x0+dial_rad*math.sin(angle)*needle[0],
            self.y0-dial_rad*math.cos(angle)*needle[0])
    
#Setting Up the meters
meters = Frame(root,width=width,height=height,bg="#03004f")
speed = Speedometer(meters,width=width,height=height)
speed.draw(min_speed,max_speed,step_speed,"Speed","KM/H")
speed.pack(side=LEFT)
meters.pack(side=LEFT, anchor=SE,fill=Y,expand=True)
meters = Frame(root,width=width,height=width,bg="#03004f")
rpm = Speedometer(meters,width=width,height=height)
rpm.draw(min_rpm,max_rpm,step_rpm,"RPM","")
rpm.pack(side=LEFT)
meters.pack(anchor=SE,fill=Y,expand=True)
setTitles()

# Digital value zone.
cSpeed=Canvas(root, width=30, height=30,bg="#03004f")
cSpeed.place(x=width*0.5,y=0.6*height)
x=Message(cSpeed, width = 100,text='')
x.place(x=0,y=0)
x.pack()
cRpm=Canvas(root, width=30, height=30,bg="#03004f")
cRpm.place(x=1.5*width,y=0.6*height)
y=Message(cRpm, width = 100,text='')
y.place(x=0,y=0)
y.pack()

#Update loop
while True:
    arr = [random.randint(0,150), random.randint(0,10000)]
    v=StringVar()
    kmph=(int)(arr[0])
    rev=(int)(arr[1])
    speed.draw_needle(kmph)
    rpm.draw_needle(rev)
    x.config(text=kmph)
    y.config(text=rev)
    root.update_idletasks()
    root.update()
    time.sleep(1)