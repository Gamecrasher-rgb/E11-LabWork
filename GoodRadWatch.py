import RPi.GPIO as GPIO  
import time
import sys
import numpy as np

GPIO.setmode(GPIO.BCM)   
GPIO.setup(17, GPIO.IN)

counts = 0

def callBack(channel):  
    global counts
    if GPIO.input(17):     # if port 17 == 1  
        print ("Count Detected!") 
        counts += 1

GPIO.add_event_detect(17, GPIO.BOTH, callback=callBack)  
  
try:  
    print ("When pressed, you'll see: Rising Edge detected on 25")  
    print ("When released, you'll see: Falling Edge detected on 25" ) 

    sleep_time = int(input("How long should the program run for: "))
    i = 0
    averageCPM = []
    while i < sleep_time:
        time.sleep(60)
        i+=1
        averageCPM.append(counts/60)
        counts = 0
    
    
finally:                   # this block will run no matter how the try block exits  
    print ("The average counts per second each minute was: ", averageCPM)

    GPIO.cleanup() 

