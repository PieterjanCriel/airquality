import numpy as np
import sensors
import pandas as pd
import datetime
import time

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
	while True:
		
		with open('out', 'a') as f:
			line = str(makeMeasurement())
			print(line)
			f.write(line+'\n')
		time.sleep(5)

if __name__ == "__main__":
    main()
