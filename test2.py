from ubidots import ApiClient
import RPi.GPIO as GPIO

api=ApiClient(token="A1E-YlhIdYEA0FzyWUEalZqae3DTJOwY1b")
variable=api.get_variable("5acca4fec03f977264abd3b1")

last_value=variable.get_values(1)

GPIO.setmode(GPIO.BCM)
print last_value[0]['value']
print "unwanted message has been stoped"
if last_value==1.0:
	print "unwanted message has been stoped"