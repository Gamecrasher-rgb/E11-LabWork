#Measures temperature, humidity, pressure
# BME280 - Adafruit#000000
#Write the data to a file - a time column, temperature, humidity, and pressure
# - Look up Adafruit CircuitPyhton BME280 module
# - update code to use that module

import time
from Adafruit_BME280 import *
import math
import csv
import numpy as np
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode = BME280_OSAMPLE_8)

temperatures = []
pressures = []
humidities = []
times = []


start_time = time.time()
run_time = 10
stop_time = start_time + run_time
current_time = time.time()


while current_time < stop_time: 
	
	temp = sensor.read_temperature()
	current_time = time.time()
	times.append(current_time)
	temperatures.append(temp)
	
	press = sensor.read_pressure()
	pressures.append(press)
	
	humid = sensor.read_humidity()
	humidities.append(humid)
	
	time.sleep(1)


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
    # writing data row-wise into the csv file
  	
    while i < length:
		writer.writerow({'Time (Unix)':times_int[i],
						'Temperatures(Celsius)':temperatures[i],
						'Pressure(Hectopascals)':pressures[i],
						'Humidity':humidities[i]})
		i = i + 1
						

 
