import RPi.GPIO as GPIO
from ubidots import ApiClient
import time
from subprocess import call
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)



while True:
	i=GPIO.input(11)
	if i==0:
		print("vibration not detected")
		
		time.sleep(1)
		api = ApiClient(token='A1E-YlhIdYEA0FzyWUEalZqae3DTJOwY1b')
		variable = api.get_variable('5acb4816c03f9776b9564805')
		response = variable.save_value({"value": i})
		
	elif i==1:
		print("vibration detected")
		call(["python","alert1.py"])
		call(["python","objectsms1.py"])
		time.sleep(1)
		api = ApiClient(token='A1E-YlhIdYEA0FzyWUEalZqae3DTJOwY1b')
		variable = api.get_variable('5acb4816c03f9776b9564805')
		response = variable.save_value({"value": i})
	call(["python","h.py"])




