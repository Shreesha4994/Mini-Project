import serial 
import time
import socket
def initialise():
	print("start")
	port = "COM4"
	s.send(bytes())
	bluetooth = serial.Serial(port,9600)
	print("connected")
	bluetooth.flushInput()
	print("DONE")
def send_data(predicted_code):
	bluetooth.write(b,str(predicted_code))
	