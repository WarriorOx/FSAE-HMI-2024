import customtkinter as ctk
from tkinter import *
import math
import time
#import sqlite3

#parameters
width = 1024
height = 600
center = [width/2,height/2]

#startup
root = ctk.CTk()
root.configure(fg_color="#1B1464")
root.geometry(f"{width}x{height}") #replace with line below when running on PI
#root.wm_attributes('-fullscreen', True)
root.resizable(False,False)
root.title("FSAE Dashboard")
root.grid_columnconfigure(2, weight=1)

#Fonts
diagnosticFont = ctk.CTkFont(family="Source Sans Pro Bold", size=14, weight="normal")
LabelFont = ctk.CTkFont(family="Source Sans Pro Bold", size=24, weight="normal")
displayFont = ctk.CTkFont(family="Source Sans Pro Bold", size=28, weight="normal")
WarningFont = ctk.CTkFont(family="Source Sans Pro Bold", size=40, weight="normal")
speedFont = ctk.CTkFont(family="Source Sans Pro Bold", size = 60, weight="normal")
#for endurance race
# make speedometer smaller, make temperature and power/lap time larger
# Add brake bias meter to both screens
# Add code to change the color of the gauges when they are above a certain number and give a error
class Endurance:

    def __init__(self):
        #Telemetry text boxes
        self.telLabels = ["Motor Temp","Bat Temp","Battery %","Power","Lap Time","Lap Power"]
        self.telNames = []
        #Text Variables
        bTvar = ctk.StringVar(value = "0°C")
        bCvar = ctk.StringVar(value = "0%")
        mTvar = ctk.StringVar(value = "0°C")
        pOvar = ctk.StringVar(value = "0 kW")
        lPvar = ctk.StringVar(value = "0:00")
        aPvar = ctk.StringVar(value = "0 kW/lap")
        self.varNames = [mTvar,bTvar,bCvar,pOvar,lPvar,aPvar]
        self.speed_val = ctk.StringVar(value="0 KM/H")

    def telemetry_make(self):
        #loop to draw all the buttons and labels
        rowData = [(2,1,5,1),(4,1,5,1),(6,1,5,1),(2,3,5,1),(4,3,5,1),(6,3,5,1)] #row,column,padx,pady
        for i in range(len(self.telLabels)):
            newlabel = ctk.CTkLabel(root, text=f'{self.telLabels[i]}',
                            text_color="#FFD239",fg_color="#1B1464",
                            width=175,height=50, font=LabelFont)
            newlabel.grid(row=rowData[i][0],column=rowData[i][1],padx=rowData[i][2],pady=rowData[i][3])

            newbutton = ctk.CTkButton(root, textvariable=self.varNames[i],
                        text_color="#FFD239",fg_color="#1B1464",
                        width=175,height=50, font=displayFont,
                        corner_radius=10, border_width=4,
                        border_color="#000000", bg_color="transparent",)
            newbutton.grid(row=rowData[i][0]+1,column=rowData[i][1],padx=rowData[i][2],pady=rowData[i][3])
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
        self.errorMSG.grid(row=1,column=1,columnspan=3,padx=5,pady=3)
        #Draw the Accelerator position and the brake pressure
        accel_label = ctk.CTkLabel(root, text="Accelerator Position",
                        text_color="#FFD239",fg_color="#1B1464",
                        width=400,height=21, font=LabelFont)
        accel_label.grid(row=2,column=2,padx=5,pady=1)

        brake_label = ctk.CTkLabel(root, text="Brake Pressure",
                        text_color="#FFD239",fg_color="#1B1464",
                        width=400,height=21, font=LabelFont)
        brake_label.grid(row=8,column=2,padx=5,pady=1)

        self.accel = ctk.CTkProgressBar(root, height=25, width=500,
                                        border_width=0,border_color="#000000",
                                        corner_radius=0,fg_color="#242424",
                                        progress_color="#FFD239",orientation="horizontal")
        self.accel.grid(row=3,column=2,padx=5,pady=1)
        self.accel.set(0)
        self.brake = ctk.CTkProgressBar(root, height=25, width=500,
                                        border_width=0,border_color="#000000",
                                        corner_radius=0,fg_color="#242424",
                                        progress_color="#FFD239",orientation="horizontal")
        self.brake.grid(row=9,column=2,padx=5,pady=1)
        self.brake.set(0)

        #speedometer canvas and placement Note: canvas size/placement changes on different screen sizes for some reason?
        self.speed_frame = Frame(root,width=650, height=325, bd=0,bg="#1B1464",highlightthickness=0)
        self.speed_frame.grid(row=4,rowspan=4,column=2,padx=5,pady=5)
        self.speed = Canvas(self.speed_frame, bd=0,bg="#1B1464",highlightthickness=0,width=650, height=325)
        self.speed.grid(row=1,column=1,rowspan=4,columnspan=3)
        #Speed digital readout is within the speedometer
        self.dig_speed = ctk.CTkLabel(self.speed_frame,textvariable=self.speed_val, text_color="#FFD239",
                            fg_color="transparent", width=300,height=75,
                            font=speedFont,corner_radius=20)
        self.dig_speed.grid(row=4,column=2)

        #Label for the screen
        self.race = ctk.CTkLabel(root, text="ENDURANCE",
                                 text_color="#FFD239",fg_color="#1B1464",
                                 width=300,height=50, font=WarningFont)
        self.race.grid(row=10,column=2,padx=5,pady=5)

    # repeatedly called function for drawing the speedometer
    def draw_speed(self,speed,max_speed,gradations,velocity):
        speed.create_oval(0,0,650,650, fill="#242424",outline="")#grey outline of speedometer (650x650)
        speed.create_arc(25,25,625,625,extent = velocity,start = 180, fill="#FFD239",outline="")#Yellow speedometer (600x600)
        speed.create_oval(50,50,600,600, fill="#1B1464",outline="")#Inner Blue oval that covers the center of the other ovals (575x575)
        circle_center = [325,325]
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
#for Acceleration, Skidpad and Autocross
class Handling:

    def __init__(self):
        #Telemetry text boxes
        self.telLabels = ["Motor Temp","Bat Temp","Battery %","Power","Acceleration","Max Accel."]
        self.telNames = []
        #Grid coordinates of buttons((x),(y))
        self.coords = [[5,844],[200,300,400]]
        #Text Variables
        bTvar = ctk.StringVar(value = "0°C")
        bCvar = ctk.StringVar(value = "0%")
        mTvar = ctk.StringVar(value = "0°C")
        pOvar = ctk.StringVar(value = "0 kW")
        aCvar = ctk.StringVar(value = "0 m/s²")
        aPvar = ctk.StringVar(value = "0 m/s²")#zero between runs with the gps home button
        self.varNames = [mTvar,bTvar,bCvar,pOvar,aCvar,aPvar]
        self.speed_val = ctk.StringVar(value="0 KM/H")
        self.yoffset = 50 #change the y value of the brake, accelerator and speedometer

    def telemetry_make(self):
        #loop to draw all the buttons and labels
        rowData = [(2,1,5,1),(4,1,5,1),(6,1,5,1),(2,3,5,1),(4,3,5,1),(6,3,5,1)] #row,column,padx,pady
        for i in range(len(self.telLabels)):
            newlabel = ctk.CTkLabel(root, text=f'{self.telLabels[i]}',
                            text_color="#FFD239",fg_color="#1B1464",
                            width=175,height=50, font=LabelFont)
            newlabel.grid(row=rowData[i][0],column=rowData[i][1],padx=rowData[i][2],pady=rowData[i][3])

            newbutton = ctk.CTkButton(root, textvariable=self.varNames[i],
                        text_color="#FFD239",fg_color="#1B1464",
                        width=175,height=50, font=displayFont,
                        corner_radius=10, border_width=4,
                        border_color="#000000", bg_color="transparent",)
            newbutton.grid(row=rowData[i][0]+1,column=rowData[i][1],padx=rowData[i][2],pady=rowData[i][3])
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
        self.errorMSG.grid(row=1,column=1,columnspan=3,padx=5,pady=3)
        #Draw the Accelerator position and the brake pressure
        accel_label = ctk.CTkLabel(root, text="Accelerator Position",
                        text_color="#FFD239",fg_color="#1B1464",
                        width=400,height=21, font=LabelFont)
        accel_label.grid(row=2,column=2,padx=5,pady=1)

        brake_label = ctk.CTkLabel(root, text="Brake Pressure",
                        text_color="#FFD239",fg_color="#1B1464",
                        width=400,height=21, font=LabelFont)
        brake_label.grid(row=8,column=2,padx=5,pady=1)

        self.accel = ctk.CTkProgressBar(root, height=25, width=500,
                                        border_width=0,border_color="#000000",
                                        corner_radius=0,fg_color="#242424",
                                        progress_color="#FFD239",orientation="horizontal")
        self.accel.grid(row=3,column=2,padx=5,pady=1)
        self.accel.set(0)
        self.brake = ctk.CTkProgressBar(root, height=25, width=500,
                                        border_width=0,border_color="#000000",
                                        corner_radius=0,fg_color="#242424",
                                        progress_color="#FFD239",orientation="horizontal")
        self.brake.grid(row=9,column=2,padx=5,pady=1)
        self.brake.set(0)

        #speedometer canvas and placement Note: canvas size/placement changes on different screen sizes for some reason?
        self.speed_frame = Frame(root,width=650, height=325, bd=0,bg="#1B1464",highlightthickness=0)
        self.speed_frame.grid(row=4,rowspan=4,column=2,padx=5,pady=5)
        self.speed = Canvas(self.speed_frame, bd=0,bg="#1B1464",highlightthickness=0,width=650, height=325)
        self.speed.grid(row=1,column=1,rowspan=4,columnspan=3)
        #Speed digital readout is within the speedometer
        self.dig_speed = ctk.CTkLabel(self.speed_frame,textvariable=self.speed_val, text_color="#FFD239",
                            fg_color="transparent", width=300,height=75,
                            font=speedFont,corner_radius=20)
        self.dig_speed.grid(row=4,column=2)

        #Label for the screen
        self.race = ctk.CTkLabel(root, text="HANDLING",
                                 text_color="#FFD239",fg_color="#1B1464",
                                 width=300,height=50, font=WarningFont)
        self.race.grid(row=10,column=2,padx=5,pady=5)

    # repeatedly called function for drawing the speedometer
    def draw_speed(self,speed,max_speed,gradations,velocity):
        speed.create_oval(0,0,650,650, fill="#242424",outline="")#grey outline of speedometer (650x650)
        speed.create_arc(25,25,625,625,extent = velocity,start = 180, fill="#FFD239",outline="")#Yellow speedometer (600x600)
        speed.create_oval(50,50,600,600, fill="#1B1464",outline="")#Inner Blue oval that covers the center of the other ovals (575x575)
        circle_center = [325,325]
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

class Testing:

    def __init__(self):
        #diagnosics Labels
        self.diaText = '''Diagnostics
Motor Temp:\nBattery Temp:\nBattery Voltage:\nBattery Current:
LV Battery Voltage:\nMotor RPM:\nBSPD Status:
BPPS Status:\nTractive Status:\nFuses:\n
'''

    def telemetry_make(self):
        self.Highlight = ctk.CTkTextbox(root,width = 500,height = 250,
                                       border_width=2,border_color="#000000",
                                       corner_radius=4,fg_color="#242424",
                                       font=diagnosticFont,
                                       text_color="#FFFFFF",wrap="word")
        self.Highlight.grid(row=0,column=0,pady=25,padx=6)
        self.Highlight.insert("0.0",text="Highlighted Data")

        self.canBox = ctk.CTkTextbox(root,width = 500,height = 250,
                                       border_width=2,border_color="#000000",
                                       corner_radius=4,fg_color="#242424",
                                       font=diagnosticFont,
                                       text_color="#FFFFFF",wrap="word")
        self.canBox.grid(row=1,column=0,pady=25,padx=6)
        self.canBox.insert("0.0",text="CAN Messages")

        self.diagnosticBox = ctk.CTkTextbox(root,width = 500,height = 550,
                                       border_width=2,border_color="#000000",
                                       corner_radius=4,fg_color="#242424",
                                       font=diagnosticFont,
                                       text_color="#FFFFFF",wrap="word")
        self.diagnosticBox.grid(row=0,rowspan=2,column=1,pady=25,padx=6)
        self.diagnosticBox.insert("0.0",text=self.diaText)


#define parameters
max_speed = 160 #max speed of the dial
gradations = 20 #gradations every X KM/H
velocity = 0 #0 to -180 speed value for the arc

screenModes = [Endurance(),Handling(),Testing()] #list of screen classes
currentMode = 0 #current screen
tmp2 = 0
diagnosticVal = ["99","45","540","150","12",
                 "9000","Good","Good","Enabled","Good"]#list of diagnostic Values
diagnosticLen = ["2.11","3.13","4.16","5.16",
                 "6.19","7.10","8.12",
                 "9.12","10.16","11.6"]#list of length of diagnostic labels
#Update loop
while True:
    #redraw the screen when mode is changed
    if not root.winfo_children():
        #print(str(currentMode) + "\n")
        screen = screenModes[currentMode]
        screen.telemetry_make()

    #tmp = bTvar.get()
    #tmp = str(int(tmp[0:-2]) + 1) + "°C"
    #bTvar.set(tmp)
    #use this to hide error message box
    #errorMSG.configure(fg_color=test, text_color="#1B1464", border_color="#1B1464")

    #code to change the color of the telemetry buttons
    #test = telNames[0]
    #test.configure(fg_color='lime')
    if currentMode !=2:
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
            screen.speed_val.set(str(tmp)+" KM/H")#classes retain their values even after screen is changed
            for widget in root.winfo_children():#clear screen
                widget.destroy()
            if currentMode < 2:#change screen mode
                currentMode +=1
            else:
                currentMode = 0
        else:
            tmp += 1
        #testing end
            screen.speed_val.set(str(tmp)+" KM/H")
    elif currentMode == 2:
        for val in range(len(diagnosticVal)):
            try:
                diagnosticVal[val] = str(int(diagnosticVal[val])-1)
            except:
                tmp=None
            finally:
                screen.diagnosticBox.delete(diagnosticLen[val],diagnosticLen[val].partition(".")[0]+".end")#delete previous value
                screen.diagnosticBox.insert(diagnosticLen[val],text=diagnosticVal[val])#write next value

        if tmp2 >= 160:
            tmp2=0
            currentMode=0
            for widget in root.winfo_children():#clear screen
                widget.destroy()
        else:
            tmp2 +=1

    time.sleep(0.01) #here to limit the update rate for testing
    
    root.update_idletasks()
    root.update()