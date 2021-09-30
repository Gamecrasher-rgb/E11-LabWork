#Measures temperature, humidity, pressure
# BME280 - Adafruit#000000
#Write the data to a file - a time column, temperature, humidity, and pressure
# - Look up Adafruit CircuitPyhton BME280 module
# - update code to use that module

import serial
import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import math
import csv
import numpy as np
import sys
import datetime as dt



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

run_time = int(input("How long should the program run for: "))

start_time = time.time()
stop_time = start_time + run_time
current_time = time.time()

sleep_time = float(input("How long should the sleep be between each data grab: "))

ready_time = int(input("In how much time are you ready (in minutes): "))
ready_time = 60*ready_time
time.sleep(ready_time)

while current_time < run_time + start_time: 
	
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

	time.sleep(sleep_time)

#Made a function to calulcate average
def average(num):
	
	avg = sum(num)/len(num)
	
	return avg
	
#Print Averages
average_temp = average(temperatures)
average_press = average(pressures)
average_humid = average(humidities)
average_pm1 = average(pm1)
average_pm25 = average(pm25)
average_pm10 = average(pm10)

times_int = []

times_int = np.array(times, dtype='int')

print('The average temperature is', average_temp)
print('The average pressure is', average_press)
print('The average humidity is', average_humid)

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
    header = ['Time (Unix)', 'Temperatures(Celsius)', 'Pressure(Hectopascals)','Humidity','pm1','pm2.5','pm10']
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()
     #writing data row-wise into the csv file
  	
    while i < length:
	    writer.writerow({'Time (Unix)':times_int[i],'Temperatures(Celsius)':temperatures[i],'Pressure(Hectopascals)':pressures[i],'Humidity':humidities[i],'pm1':pm1[i],'pm2.5':pm25[i],'pm10':pm10[i]})
	    i+=1
				
