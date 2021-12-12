from ubidots import ApiClient
import math
import time
import serial

a="12.9077"
b="80.1422"
api = ApiClient(token='A1E-YlhIdYEA0FzyWUEalZqae3DTJOwY1b')
variable = api.get_variable('5acb4861c03f97772987d93c')
response = variable.save_value({'value':10, 'context':{'lat': a, 'lng': b}})

