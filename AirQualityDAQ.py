#Air Quality Script
import serial
import time
import board
import math
import csv
import numpy as np


start_time = time.time()
run_time = 10
stop_time = start_time + run_time
current_time = time.time()

pm1 = []
pm25 = []
pm10 = []
times = []

while current_time < stop_time: 
	
	port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.5)
	text = port.read(32)
	
	current_time = time.time()
	times.append(current_time)
	
	pmtemp1 = int.from_bytes(text[4:6], byteorder='big')
	pm1.append(pmtemp1)
	
	pmtemp25 = int.from_bytes(text[5:7], byteorder='big')
	pm25.append(pmtemp25)
	
	pmtemp10 = int.from_bytes(text[8:10], byteorder='big')
	pm10.append(pmtemp10)
	
	time.sleep(1)

times_int = []

times_int = np.array(times, dtype='int')

file = open('AirQualityData.csv', 'w')
length = len(times)
print(length)
i = 0

with file:
    # identifying header  
    header = ['Time(Unix)','pm1', 'pm2.5', 'pm10']
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()
     #writing data row-wise into the csv file
  	
    while i < length:
	    writer.writerow({'Time(Unix)':times[i],'pm1':pm1[i],'pm2.5':pm25[i],'pm10':pm10[i]})
	    i+=1

