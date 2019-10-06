#!/usr/bin/python

from datetime import datetime
import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
import string
import random

def generate_clientId():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(8))

def read_sensor():
    #pin = 4
    #humidity, temperature = Adafruit_DHT.read_retry(str(sensor), pin)
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
    temperature = round(temperature, 1)
    humidity = round(humidity, 1)
    fdatatime = (((datetime.now() - datetime(1970, 1, 1)).total_seconds()) + 14400)
    sdatatime = str(round(fdatatime, 0))[0:-2]
    ret = '{ "datetime:", "' + sdatatime + '", "temperature:"' + str(temperature) +'", "humidity:" , "' + str(humidity) + '" }'
    return(ret)

def main():
    clientId = generate_clientId()
    client = mqtt.Client(clientId)
    client.connect("192.168.1.78", 1883)
    data = read_sensor()
    print(data)
    client.publish("weather/office", str(data), qos = 0, retain = True)
    
if __name__=='__main__':
    main()


