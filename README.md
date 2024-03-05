# FSAE-HMI-2024
Code for obtaining data from CAN bus and i2c, storing the data in a SQLite database and displaying relevant data on a screen for the driver.

## Data Aquired/Stored
- Speed (calcuated from motor RPM and gear ratio)
- Motor temperature
- Coolant Temperature (4x Thermocouple)
- Coolant Flow Rate
- Motor current
- Battery Voltage
- Battery Temperature
- LV Battery Voltage (need a module for this still)
- GPS Location
- Acceleration 3-axis
- Direction 3-axis
- Lap time (endurance only)

## How It Works
#### Main_Screen.py
The screen is connected to a Raspberry Pi (henceforth Rpi) by HDMI that is under the dash. The Rpi communicates with the gps and gyroscope + accelerometer combo unit over i2c. Additionally, the thermocouples are connected to the i2c network through a differential i2c bus from the rear of the car. The gyroscope and gps may be moved to the rear of the car depending on mounting/positioning. The Rpi is also connected to the CAN bus over spi that is level shifted to 5V. The CAN bus is connected to the VCU directly.
#### Database.py
The database is a SQLite database running on the Rpi and is stored on the Rpi's SD card. It logs the data at a set frequency and stores it in the database along with a timestamp.
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

See library documentation for information on how to use