#Measures temperature, humidity, pressure
# BME280 - Adafruit#000000
#Write the data to a file - a time column, temperature, humidity, and pressure
# - Look up Adafruit CircuitPyhton BME280 module
# - update code to use that module

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

times = []


run_time = int(input("How long should the program run for (in minutes): "))

sleep_time = float(input("How long should the sleep be between each data grab: "))

ready_time = int(input("In how much time are you ready (in minutes): "))
ready_time = 60*ready_time
time.sleep(ready_time)

start_time = time.time()
stop_time = start_time + (run_time*60)
current_time = time.time()

GPIO.add_event_detect(17, GPIO.BOTH, callback=callBack) 

averageCPS = 0
listaverageCPS = []
i = 0

while current_time < run_time*60 + start_time: 

	current_time = time.time()
	times.append(current_time)
	
	averageCPS = counts/(sleep_time*60)
	listaverageCPS.append(averageCPS)
	counts = 0

	time.sleep(sleep_time)

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
    header = ['Time (Unix)','CPS']
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()
     #writing data row-wise into the csv file
  	
    while i < length:
	    writer.writerow({'Time (Unix)':times_int[i],'CPS':listaverageCPS[i]})
	    i+=1
				
