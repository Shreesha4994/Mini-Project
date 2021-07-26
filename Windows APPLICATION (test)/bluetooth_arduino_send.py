import serial 
import time
print("start")
port = "COM4"
bluetooth = serial.Serial(port,9600)
print("connected")
bluetooth.flushInput()
print("DONE")
