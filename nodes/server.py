#!/usr/bin/python

# Requirement: Python 2.7

import Adafruit_DHT
import httplib2
from apiclient.discovery import build
import datetime
from oauth2client import client
from oauth2client.file import Storage
from oauth2client import tools
import argparse
import ConfigParser
import os
filepath = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(parents=[tools.argparser])
flags = parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(filepath + '.env')

def readDHT22(pin, show=False):
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        if (show):
            print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
        return temperature, humidity
    else:
        print 'Failed to get reading. Try again!'

def googlePOST(temperature, humidity):
    flow = client.flow_from_clientsecrets(
	config.get('Config', 'client_secrets_file'),
    scope='https://www.googleapis.com/auth/fusiontables')
    http = httplib2.Http()
    storage = Storage('sec_storage.enc')
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    flags = parser.parse_args()
    if(storage.get()):
        credentials = storage.get()
    else:
        credentials = tools.run_flow(flow, storage, flags)
    storage.put(credentials)
    http_auth = credentials.authorize(http)
    service = build('fusiontables', 'v2',developerKey=config.get('Config', 'google_api_key'), http=http_auth)
    query = service.query()
    sqlstring = "INSERT INTO {:s} (nodeid, temperature, humidity, date) VALUES ({:d}, {:f}, {:f}, '{:s}');".format(config.get('Config', 'table_id'), 1, temperature, humidity, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    query.sql(sql=sqlstring).execute()

def main():
    temp, hum = readDHT22(4);
    googlePOST(temp, hum)

 
if __name__ == "__main__":
    main()
