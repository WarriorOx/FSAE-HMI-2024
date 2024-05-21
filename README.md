# FSAE-HMI-2024
Code for main driver screen, datalogging and VCU controls

## Data Aquired/Stored
- Speed (calcuated from motor RPM and gear ratio on VCU)
- Motor temperature
- Coolant Temperature (3x Thermocouple)
- Coolant Flow Rate
- Motor current
- Battery Voltage
- Battery Temperature
- LV Battery Voltage
- GPS Location (logitude, Latitude)
- Acceleration 3-axis (Yaw, Pitch, Roll)
- Direction 3-axis (X, Y, Z)
- Max Acceleration (Handling Events only)
- Top Speed (Reset from function button)
- Drive mode (Drive or Neutral)
- Lap time (endurance only)

## How It Works
#### Main_Screen.py
The screen is connected to a Raspberry Pi (henceforth Rpi) by HDMI that is under the dash. The Rpi is connected to the CAN bus over spi that is level shifted to 5V. The CAN bus is connected to the VCU directly. This script recieves all sensor data from the VCU and logs the data to the database along with a unique id and timestamp. This script also handles the switch screen button and the screen function button (reset). Additionally, this code calculates the top speed, lap time, max acceleration, battery charge %, power and lap power (avg power for the lap*lap time -> kWh) from the data it recieves.
#### VCU Code
This code interfaces with the HV CAN loop to collect data from the inverter, BMS and motor over CAN. It also handles the interrupt for the Drive/Neutral button and LED. All Sensor data will be collected by the VCU and sent to the Raspberry Pi over a seperate CAN loop. The VCU will interface with the I2C bus over differential I2C, which will be connected to the 3x thermocouples, GPS, Accelerometer/Gyroscope and Magnetometer. The VCU will also control 4 relays and a number of GPIOs/ADCs will be used to collect analog sensor data and send signals.
#### Unmade-file.py
This file converts the data from the database to different graphs and an excel or csv file(undecided) and saves the files to the SD Card. A USB stick can be plugged into the Rpi to copy the data over.

## Libraries
| Library | Usage |
|---------|-------|
|Tkinter and customTkinter | Screen & UI |
|sqlite3 | Database Interfacing |
|adafruit-circuitpython-lsm6ds | Accelerometer and Gyroscope |
|adafruit-circuitpython-gps | GPS Module |
|adafruit-circuitpython-mmc56x3 | Magnetometer |
|RPi.GPIO | Raspberry Pi's GPIO & Interrupts |

See library documentation for information on how to use