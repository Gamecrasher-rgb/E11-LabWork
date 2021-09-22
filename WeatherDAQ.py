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

if len(sys.argv) > 1:
  run_time = int(sys.argv[1])
  if len(sys.argv) > 2:
    sleep_time = int(sys.argv[2])

start_time = time.time()
stop_time = start_time + run_time
current_time = time.time()


while current_time < run_time + start_time: 
	
	temp = bme280.temperature
	current_time = time.time()
	times.append(current_time)
	temperatures.append(temp)
	
	press = bme280.pressure
	pressures.append(press)
	
	humid = bme280.relative_humidity
	humidities.append(humid)
	
	port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.5)
	text = port.read(32)
	
	pmtemp1 = int.from_bytes(text[4:6], byteorder='big')
	pm1.append(pmtemp1)
	
	pmtemp25 = int.from_bytes(text[5:7], byteorder='big')
	pm25.append(pmtemp25)
	
	pmtemp10 = int.from_bytes(text[8:10], byteorder='big')
	pm10.append(pmtemp10)

	time.sleep(0.5)

#Made a function to calulcate average
def average(num):
	
	avg = sum(num)/len(num)
	
	return avg
	
#Print Averages
average_temp = average(temperatures)
average_press = average(pressures)
average_humid = average(humidities)

times_int = []

times_int = np.array(times, dtype='int')

print('The average temperature is', average_temp)
print('The average pressure is', average_press)
print('The average humidity is', average_humid)

file = open('SensorData.csv', 'w')

length = len(times)
print(length)
i = 0

with file:
    # identifying header  
    header = ['Time (Unix)', 'Temperatures(Celsius)', 'Pressure(Hectopascals)','Humidity','Air Quality','pm1','pm2.5','pm10']
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()
     #writing data row-wise into the csv file
  	
    while i < length:
	    writer.writerow({'Time (Unix)':times_int[i],'Temperatures(Celsius)':temperatures[i],'Pressure(Hectopascals)':pressures[i],'Humidity':humidities[i],'pm1':pm1[i],'pm2.5':pm25[i],'pm10':pm10[i]})
	    i+=1
						

 
