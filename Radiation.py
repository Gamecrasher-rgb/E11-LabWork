import time
import datetime
import RPI.GPIO as GPIO

def Int21R( channel ):
  global Count

  Count += 1
  GPIO.output( 20, GPIO.HIGH )
  time.sleep( 0.000001 )
  GPIO.output( 20, GPIO.LOW )


GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )

GPIO.setup( 20, GPIO.OUT )
GPIO.setup( 21, GPIO.IN, pull_up_down = GPIO.PUD_OFF )
GPIO.add_event_detect( 21, GPIO.RISING, callback = Int21R )

Count = 0
while True:
  Time = datetime.datetime.now()
  print( "%s - Count = %6d  RPM = %6d" % ( Time, Count, Count * 60.0 ) )
  RPM = Count * 60.0
  Count = 0
  t = time.time( )
  Wait = 1 - ( t - int( t ) )
  time.sleep( Wait )

GPIO.cleanup( )
