from ubidots import ApiClient
import random
import time
from subprocess import call
api = ApiClient(token='A1E-YlhIdYEA0FzyWUEalZqae3DTJOwY1b')
variable = api.get_variable("5acca4fec03f977264abd3b1")
while(1):
        laf = variable.get_values()
        print laf
        a = laf[0]['value']
        print a
        if a==1.0:
        	print "motor on"
        else:
                print "motor off"




