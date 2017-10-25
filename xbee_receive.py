import time
from hachi.serial import XBeeSerial
x = XBeeSerial('/dev/ttyUSB0')
while True:
	#time.sleep(0)
	print("<<<<<")
	data = x.read_response()
	print("%s celsius" % data.data.decode('utf-8'))
