#!/usr/bin/env python

import requests
import time
from pms5003 import PMS5003, ReadTimeoutError

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

try:
    bus = SMBus(1)
except Exception as e:
    print(e)

# Create PMS5003 instance
try:
    pms5003 = PMS5003(device='/dev/ttyS0')
except Exception as e:
    print(e)


# Read values from BME280 and PMS5003 and return as dict
def read_values():
    values = {}
    try:
        pm_values = pms5003.read()
        print(pm_values)
        values["P2"] = str(pm_values.pm_ug_per_m3(2.5))
        values["P1"] = str(pm_values.pm_ug_per_m3(10))
    except ReadTimeoutError:
        pms5003.reset()
        pm_values = pms5003.read()
        values["P2"] = str(pm_values.pm_ug_per_m3(2.5))
        values["P1"] = str(pm_values.pm_ug_per_m3(10))
    return values


# Main loop to read data and send to Luftdaten
while True:
    values = None
    try:
        values = read_values()
        #print(values)
        time.sleep(1)
    except Exception as e:
        print(e)
