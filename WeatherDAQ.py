#Measures Temperature, Humidity, Pressure, Air Quality, and Radiation

#region imports
import serial
import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import math
import csv
import numpy as np
import sys
import datetime as dt
import RPi.GPIO as GPIO  
#endregion

GPIO.setmode(GPIO.BCM)   
GPIO.setup(17, GPIO.IN)

counts = 0

def callBack(channel):  
    global counts
    if GPIO.input(17):     # if port 17 == 1  
        print ("Count Detected!") 
        counts += 1

i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

temperatures = []
pressures = []
humidities = []
times = []
pm1 = []
pm25 = []
pm10 = []

bme280.sea_level_pressure = 1013.25

run_time = int(input("How long should the program run for (in minutes): "))

sleep_time = float(input("How long should the sleep be between each data grab(in minutes): "))

ready_time = int(input("In how much time are you ready (in minutes): "))
ready_time = 60*ready_time
time.sleep(ready_time)

start_time = time.time()
stop_time = start_time + run_time
current_time = time.time()

GPIO.add_event_detect(17, GPIO.BOTH, callback=callBack) 

averageCPS = 0
listaverageCPS = []
n = 0

while n < run_time: 
	time.sleep(sleep_time*60)

	current_time = time.time()
	times.append(current_time)

	temp = bme280.temperature
	temperatures.append(temp)
	
	press = bme280.pressure
	pressures.append(press)
	
	humid = bme280.relative_humidity
	humidities.append(humid)
	
	port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.5)
	text = port.read(32)
	
	pmtemp1 = int.from_bytes(text[4:6], byteorder='big')
	pm1.append(pmtemp1)
	
	pmtemp25 = int.from_bytes(text[6:8], byteorder='big')
	pm25.append(pmtemp25)
	
	pmtemp10 = int.from_bytes(text[8:10], byteorder='big')
	pm10.append(pmtemp10)
	
	averageCPS = counts/(sleep_time)
	listaverageCPS.append(averageCPS)
	counts = 0
	n+=1

GPIO.cleanup()

#Made a function to calulcate average
def average(num):
	
	avg = sum(num)/len(num)
	
	return avg

print("Done!")

times_int = []

times_int = np.array(times, dtype='int')

dateCreation = dt.datetime.now()
print(dateCreation)
dateCreation = str(dateCreation.replace(microsecond = 0))
def remove(string):
    return string.replace(" ", "--")
date = remove(dateCreation)

filename = 'SensorData--' + date + '.csv'

file = open(filename, 'w')

length = len(times)
i = 0

with file:
    # identifying header  
    header = ['Time (Unix)', 'Temperatures(Celsius)', 'Pressure(Hectopascals)','Humidity','pm1','pm2.5','pm10','CPM']
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()
     #writing data row-wise into the csv file
  	
    while i < length:
	    writer.writerow({'Time (Unix)':times_int[i],'Temperatures(Celsius)':temperatures[i],'Pressure(Hectopascals)':pressures[i],'Humidity':humidities[i],'pm1':pm1[i],'pm2.5':pm25[i],'pm10':pm10[i],'CPM':listaverageCPS[i]})
	    i+=1
				
