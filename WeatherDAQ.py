#Measures temperature, humidity, pressure
# BME280 - Adafruit#000000
#Write the data to a file - a time column, temperature, humidity, and pressure
# - Look up Adafruit CircuitPyhton BME280 module
# - update code to use that module

import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import math
import csv
import numpy as np

i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

temperatures = []
pressures = []
humidities = []
times = []

bme280.sea_level_pressure = 1013.25

start_time = time.time()
run_time = 10
stop_time = start_time + run_time
current_time = time.time()


while current_time < stop_time: 
	
	temp = bme280.temperature
	current_time = time.time()
	times.append(current_time)
	temperatures.append(temp)
	
	press = bme280.pressure
	pressures.append(press)
	
	humid = bme280.relative_humidity
	humidities.append(humid)
	
	time.sleep(1)

#Made a function to calulcate average
def average(num):
	
	avg = sum(num)/len(num)
	
	return avg
	
	
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
    header = ['Time (Unix)', 'Temperatures(Celsius)', 'Pressure(Hectopascals)','Humidity']
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()
     #writing data row-wise into the csv file
  	
    while i < length:
	    writer.writerow({'Time (Unix)':times_int[i],'Temperatures(Celsius)':temperatures[i],'Pressure(Hectopascals)':pressures[i],'Humidity':humidities[i]})
	    i+=1
						

 
