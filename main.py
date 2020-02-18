import numpy as np
import sensors
import pandas as pd
import datetime
import time
import sys
import  os
from datadog import initialize, api

apiKey = os.environ['DD_API_KEY']
location = sys.argv[1]
sleep_interval = sys.argv[2]

options = {
    'api_key': apiKey
}

initialize(**options)


particleSensor = sensors.ParticleSensor()
temperatureSentor = sensors.TemperatureSentor()

def makeMeasurement():
    ts = datetime.datetime.now()
    particleData = particleSensor.read()
    temperatureData = temperatureSentor.read()
    
    data = dict()
    data.update(particleData)
    data.update(temperatureData)
    
    return data
    

def main():
    while True:
        data = makeMeasurement()
        for metric_key, metric_value in data.items():
	        api.Metric.send(
	        	metric='showpad.meteo.{metric_key}'.format(metric_key=metric_key),
	        	points=metric_value,
	        	tags=["location:"+location]
	        	)

        time.sleep(int(sleep_interval))

if __name__ == "__main__":
    main()
