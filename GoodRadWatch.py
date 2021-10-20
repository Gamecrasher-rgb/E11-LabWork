import RPi.GPIO as GPIO  
import time

GPIO.setmode(GPIO.BCM)   
GPIO.setup(17, GPIO.IN)

counts = 0

def callBack(channel):  
    global counts
    if GPIO.input(17):     # if port 17 == 1  
        print ("Count Detected!") 
        counts =+ 1 
    else:                  # if port 17 != 1  
        print ("Count Gone...")  

GPIO.add_event_detect(17, GPIO.BOTH, callback=callBack)  
    
input("Press Enter when ready\n>")  
  
try:  
    print ("When pressed, you'll see: Rising Edge detected on 25")  
    print ("When released, you'll see: Falling Edge detected on 25" ) 
    #run_time = int(input("How long should the program run for: "))

    #sleep_time = float(input("How long should the sleep be between each data grab: "))

    ready_time = int(input("In how much time are you ready (in minutes): "))
    ready_time = 60*ready_time
    time.sleep(ready_time)

    #start_time = time.time()
    #stop_time = start_time + run_time
    #current_time = time.time()       
finally:                   # this block will run no matter how the try block exits  
    print ("The average counts per minute was", counts / (ready_time/60))
    GPIO.cleanup() 

