#Air Quality Script
import serial
port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.5)

text = port.read(32)

pm1 = int.from_bytes(text[3:5], byteorder='big')
pm2 = int.from_bytes(text[5:7], byteorder='big')
pm3 = int.from_bytes(text[7:9], byteorder='big')

pm4 = int.from_bytes(text[17:19], byteorder='big')
