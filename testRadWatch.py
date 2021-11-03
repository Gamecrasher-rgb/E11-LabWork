#Measures Temperature, Humidity, Pressure, Air Quality, and Radiation

#region imports
import serial
import time
import board
import csv
import numpy as np
import sys
import datetime as dt
import RPi.GPIO as GPIO  
#endregion

GPIO.setmode(GPIO.BCM)   
GPIO.setup(17, GPIO.IN)

times = []
counts = 0

def callBack(channel):  
    global counts
    if GPIO.input(17):   
        counts += 1


run_time = int(sys.argv[1])

sleep_time = float(sys.argv[2])

ready_time = int(sys.argv[3])
ready_time = 60*ready_time
time.sleep(ready_time)

start_time = time.time()
stop_time = start_time + run_time
current_time = time.time()

GPIO.add_event_detect(17, GPIO.BOTH, callback=callBack) 

averageCPM = 0
averageCPS = 0
listaverageCPS = []
listaverageCPM = []
n = 0

while n < run_time: 
	time.sleep(sleep_time*60)
	averageCPM = counts
	averageCPS = counts/60
	listaverageCPS.append(averageCPS)
	listaverageCPM.append(averageCPM)
	counts = 0
	n+=1

GPIO.cleanup()

print("Done!")

times_int = []

times_int = np.array(times, dtype='int')

dateCreation = dt.datetime.now()
dateCreation = str(dateCreation.replace(microsecond = 0))
def remove(string):
    return string.replace(" ", "--")
date = remove(dateCreation)

filename = 'RadiationData--' + date + '.csv'

print("File Name:",filename)

file = open(filename, 'w')

length = len(times)
i = 0

with file:
    header = ['Time (Unix)','CPS','CPM']
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()
  	
    while i < length:
	    writer.writerow({'Time (Unix)':times_int[i],'CPS':listaverageCPS[i],'CPM':listaverageCPM[i]})
	    i+=1
				
