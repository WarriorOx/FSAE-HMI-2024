import customtkinter as ctk
from tkinter import *
import math
import time
import sqlite3

#parameters
width = 1024
height = 600
center = [width/2,height/2]

#startup
root = ctk.CTk()
root.configure(fg_color="#1B1464")
root.geometry(f"{width}x{height}") #replace with line below when running on PI
#root.wm_attributes('-fullscreen', True)
root.title("FSAE Dashboard")

#Fonts
LabelFont = ctk.CTkFont(family="Source Sans Pro Bold", size=24, weight="normal")
displayFont = ctk.CTkFont(family="Source Sans Pro Bold", size=28, weight="normal")
WarningFont = ctk.CTkFont(family="Source Sans Pro Bold", size=40, weight="normal")
speedFont = ctk.CTkFont(family="Source Sans Pro Bold", size = 60, weight="normal")

class Endurance:

    def __init__(self):
        #Telemetry text boxes
        self.telLabels = ["Motor Temp","Lap Time","Battery %","Power Output","Battery Temp","Lap Power"]
        self.telNames = []
        #Grid coordinates of buttons((x),(y))
        self.coords = [[5,819],[200,300,400]]
        #Text Variables
        bTvar = ctk.StringVar(value = "0°C")
        bCvar = ctk.StringVar(value = "0%")
        mTvar = ctk.StringVar(value = "0°C")
        pOvar = ctk.StringVar(value = "0 kW")
        lPvar = ctk.StringVar(value = "0:00")
        aPvar = ctk.StringVar(value = "0 kW AVG")
        self.varNames = [mTvar,lPvar,bCvar,pOvar,bTvar,aPvar]
        self.speed_val = ctk.StringVar(value="0 KM/H")

    def telemetry_make(self):
        #loop to draw all the buttons and labels
        for i in range(len(self.telLabels)):
            newlabel = ctk.CTkLabel(root, text=f'{self.telLabels[i]}',
                            text_color="#FFD239",fg_color="#1B1464",
                            width=200,height=50, font=LabelFont)
            newlabel.place(x=self.coords[0][math.floor(i/3)],y=self.coords[1][i%3])

            newbutton = ctk.CTkButton(root, textvariable=self.varNames[i],
                        text_color="#FFD239",fg_color="#1B1464",
                        width=200,height=50, font=displayFont,
                        corner_radius=10, border_width=4,
                        border_color="#000000", bg_color="transparent",)
            newbutton.place(x=self.coords[0][math.floor(i/3)],y=self.coords[1][i%3] + 50)
            self.telNames.append(newbutton)
        #draw the error message button
        error = ctk.StringVar(value = "Initial Value")
        self.isError = False
        self.prevError = False
        self.errorMSG = ctk.CTkButton(root, textvariable=error,
                                text_color="black",fg_color='red',
                                width=800,height=60, font=WarningFont,
                                corner_radius=10, border_width=4,
                                border_color="#000000", bg_color="transparent")
        self.errorMSG.place(x=112, y=10)
        #Draw the Accelerator position and the brake pressure
        accel_label = ctk.CTkLabel(root, text="Accelerator Position",
                        text_color="#FFD239",fg_color="#1B1464",
                        width=400,height=21, font=LabelFont)
        accel_label.place(x=312,y=72)

        brake_label = ctk.CTkLabel(root, text="Brake Pressure",
                        text_color="#FFD239",fg_color="#1B1464",
                        width=400,height=21, font=LabelFont)
        brake_label.place(x=312,y=422)

        self.accel = ctk.CTkProgressBar(root, height=25, width=500,
                                        border_width=0,border_color="#000000",
                                        corner_radius=0,fg_color="#242424",
                                        progress_color="#FFD239",orientation="horizontal")
        self.accel.place(x = 262, y = 100)
        self.accel.set(0)
        self.brake = ctk.CTkProgressBar(root, height=25, width=500,
                                        border_width=0,border_color="#000000",
                                        corner_radius=0,fg_color="#242424",
                                        progress_color="#FFD239",orientation="horizontal")
        self.brake.place(x = 262, y = 450)
        self.brake.set(0)

        #speedometer canvas and placement Note: canvas size/placement changes on different screen sizes for some reason?
        self.speed = Canvas(root,width=800, height=350, bd=0,bg="#1B1464",highlightthickness=0)
        self.speed.place(x=224, y=150)
        #Speed digital readout
        self.dig_speed = ctk.CTkLabel(root,textvariable=self.speed_val, text_color="#FFD239",
                            fg_color="transparent", width=300,height=75,
                            font=speedFont,corner_radius=20)
        self.dig_speed.place(x = (1024-300)/2,y = 250)

    # repeatedly called function for drawing the speedometer
    def draw_speed(self,speed,max_speed,gradations,velocity):
        speed.create_oval(75,25,725,675, fill="#242424",outline="")#grey outline of speedometer (650x650)
        speed.create_arc(100,50,700,650,extent = velocity,start = 180, fill="#FFD239",outline="")#Yellow speedometer (600x600)
        speed.create_oval(125,75,675,625, fill="#1B1464",outline="")#Inner Blue oval that covers the center of the other ovals (575x575)
        circle_center = [400,350]
        #Loop to draw gradations
        for i in range(int(max_speed/5)+1):
            angle = i*math.pi/((max_speed/5))
            xangle = math.cos(angle)
            yangle = -math.sin(angle)
            if (i*5)%gradations == 0:#major Dimension
                speed.create_line(circle_center[0]+324*xangle,circle_center[1]+324*yangle,
                                circle_center[0]+310*xangle,circle_center[1]+310*yangle,fill="#FFD239",width=4)
                
            else:#minor dimension
                speed.create_line(circle_center[0]+324*xangle,circle_center[1]+324*yangle,
                                circle_center[0]+315*xangle,circle_center[1]+315*yangle,fill="#FFD239",width=2)

screen = Endurance()
screen.telemetry_make()

#define parameters
max_speed = 160 #max speed of the dial
gradations = 20 #gradations every X KM/H
velocity = 0 #0 to -180 speed value for the arc

#Update loop
while True:
    #tmp = bTvar.get()
    #tmp = str(int(tmp[0:-2]) + 1) + "°C"
    #bTvar.set(tmp)
    #use this to hide error message box
    #errorMSG.configure(fg_color=test, text_color="#1B1464", border_color="#1B1464")

    #code to change the color of the telemetry buttons
    #test = telNames[0]
    #test.configure(fg_color='lime')

    tmp = screen.accel.get() + 0.005
    if tmp >=1:
        tmp=0
    screen.accel.set(tmp)

    tmp = screen.brake.get() + 0.005
    if tmp >=1:
        tmp=0
    screen.brake.set(tmp)

    tmp=int(screen.speed_val.get()[0:-5])
    velocity = -(tmp/max_speed)*180 #convert speed to degrees
    screen.speed.delete("all") #clear canvas before re-drawing to save memory/speed
    screen.draw_speed(screen.speed,max_speed,gradations,velocity)
    #testing
    if tmp == 160:
        tmp = 0
    else:
        tmp += 1
    #testing end
    screen.speed_val.set(str(tmp)+" KM/H")
    time.sleep(0.01) #here to limit the update rate for testing
    
    root.update_idletasks()
    root.update()