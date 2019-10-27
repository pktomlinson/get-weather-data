#!/usr/bin/python
#
# reads data from AM2303 temperature and humidity
# sensor using Adafruit_DHT library.
# connects to local mqtt broker and broadcasts
# results
#
# import required modules and libraries
from datetime import datetime
import Adafruit_DHT
import paho.mqtt.client as mqtt
import string
import random

# generate a random clientId for connecting to mqtt broker
def generate_clientId():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(8))

# read_sensor - requires sensor object and pin #
def read_sensor(sensor, pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = round(temperature, 1)
    humidity = round(humidity, 1)
    # +14400 adds 4 hours to GMT to reflect my timezone
    # that is a bad hack and I should resolve issue with python functionality
    fdatatime = (((datetime.now() - datetime(1970, 1, 1)).total_seconds()) + 14400)
    sdatatime = str(round(fdatatime, 0))[0:-2]
    ret = '{ "datetime:", "' + sdatatime + '", "temperature:"' + str(temperature) +'", "humidity:" , "' + str(humidity) + '" }'
    return(ret)

# main - generates cliendId
#        creates client object
#        connects to local broker
#        reads sensor
#        publish returned json data
#        disconnects from broker
def main():
    clientId = generate_clientId()
    client = mqtt.Client(clientId)
    client.connect("localhost", 1883)
    data = read_sensor(Adafruit_DHT.AM2302, 4)
    print(data)
    client.publish("weather/office", str(data), qos = 0, retain = True)
    client.disconnect()

# init program
if __name__=='__main__':
    main()
