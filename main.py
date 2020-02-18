import numpy as np
import sensors
import pandas as pd
import datetime
import time
import sys
import  os
from datadog import initialize, api

apiKey = os.environ['DD_API_KEY']
appKey = os.environ['DD_APP_KEY']
location = sys.argv[1]

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
    
    d = {"timestamp": ts}
    d.update(particleData)
    d.update(temperatureData)
    
    return d
    

def main():
    print(apiKey)
    print(appKey)
    print(location)
    while True:
        data = makeMeasurement()
        api.Metric.send(metric='showpad.meteo.temperature', points=data['temperature'], tags=["location:"+location])
        print(str(data['temperature']))
        time.sleep(5)

if __name__ == "__main__":
    main()
