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

#Telemetry text boxes
telLabels = ["Battery Temp","Battery Charge","Motor Temp","Power Output","Battery Voltage","Motor RPM"]
telNames = []
#Grid coordinates ((x),(y))
coords = [[156,412,668],[350,475]]
#Text Variables
bTvar = ctk.StringVar(value = "0°C")
bCvar = ctk.StringVar(value = "0%")
mTvar = ctk.StringVar(value = "0°C")
pOvar = ctk.StringVar(value = "0 kW")
pVvar = ctk.StringVar(value = "0 V")
mRvar = ctk.StringVar(value = "0 RPM")
varNames = [bTvar,bCvar,mTvar,pOvar,pVvar,mRvar]

def telemetry_make():
    for i in range(6):
        newlabel = ctk.CTkLabel(root, text=f'{telLabels[i]}',
                          text_color="#FFD239",fg_color="#1B1464",
                          width=200,height=50, font=LabelFont)
        newlabel.place(x=coords[0][i%3],y=coords[1][math.floor(i/3)])

        newbutton = ctk.CTkButton(root, textvariable=varNames[i],
                      text_color="#FFD239",fg_color="#1B1464",
                      width=200,height=50, font=displayFont,
                      corner_radius=10, border_width=4,
                      border_color="#000000", bg_color="transparent",)
        newbutton.place(x=coords[0][i%3],y=coords[1][math.floor(i/3)] + 50)
        telNames.append(newbutton)

telemetry_make()
#Error Message/Warnings
error = ctk.StringVar(value = "placeholder")
isError = False
prevError = False
errorMSG = ctk.CTkButton(root, textvariable=error,
                         text_color="black",fg_color='red',
                         width=800,height=75, font=WarningFont,
                         corner_radius=10, border_width=4,
                         border_color="#000000", bg_color="transparent")
errorMSG.place(x=112, y=10)
test = 'transparent'

#speedometer

#define parameters
max_speed = 200 #max speed of the dial
gradations = 20 #gradations every X KM/H
velocity = 0 #0 to -180 speed value for the arc

#speedometer canvas and placement
speed = Canvas(root,width=800, height=325, bd=0,bg="#1B1464",highlightthickness=0)
speed.place(x=224, y=115)

# repeatedly called function for drawing the speedometer
def draw_speed(speed,max_speed,gradations,velocity):
    speed.create_oval(75,25,725,650, fill="#242424",outline="")
    speed.create_arc(100,50,700,650,extent = velocity,start = 180, fill="#FFD239",outline="")
    speed.create_oval(125,75,675,650, fill="#1B1464",outline="")
    circle_center = [400,325] #325 kinda fixes it
    #Loop to draw gradations
    '''
    for i in range(int(max_speed/5)+1):
        angle = i*math.pi/((max_speed/5))
        xangle = math.cos(angle)
        yangle = -math.sin(angle)
        if (i*5)%gradations == 0:
            speed.create_line(circle_center[0]+325*xangle,circle_center[1]+325*yangle,
                              circle_center[0]+305*xangle,circle_center[1]+305*yangle,fill="#FFD239",width=2)
            #need to change to work with canvas grid
            
        else:
            tmp=None#minor dimension
    '''
speed_val = ctk.StringVar(value="0 KM/H")
dig_speed = ctk.CTkLabel(root,textvariable=speed_val, text_color="#FFD239",
                    fg_color="transparent", width=300,height=75,
                    font=speedFont,corner_radius=20)
dig_speed.place(x = (1024-300)/2,y = 250)

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

    tmp=int(speed_val.get()[0:-5])
    velocity = -(tmp/max_speed)*176
    speed.delete("all") #clear canvas before re-drawing to save memory/speed
    draw_speed(speed,max_speed,gradations,velocity)
    #testing
    if tmp == 200:
        tmp = 0
    else:
        tmp+=1
    #testing end
    speed_val.set(str(tmp)+" KM/H")
    time.sleep(0.01) #here to limit the update rate for testing
    
    root.update_idletasks()
    root.update()