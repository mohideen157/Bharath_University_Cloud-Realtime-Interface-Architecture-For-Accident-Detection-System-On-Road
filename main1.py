from ubidots import ApiClient
import math
import time
import serial
while(1):
	ser = serial.Serial('/dev/ttyACM0', 9600)
	z = ser.readline()
	print z
	if 'pressure:' in  z : 
		d = z[9:18]
		print d
		api = ApiClient(token='A1E-YlhIdYEA0FzyWUEalZqae3DTJOwY1b')
		variable = api.get_variable('5acb47eec03f9775f9650485')
		response = variable.save_value({"value": d})

	if 'SOS ON:' in  z : 
		call(["python","objectsms1.py"])

