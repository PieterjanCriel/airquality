#!/usr/bin/env python

import requests
import sys
from pms5003 import PMS5003, ReadTimeoutError

DEVICE = '/dev/ttyS0'

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

try:
    bus = SMBus(1)
except Exception as e:
    sys.stderr.write(e)
    exit(1)

class ParticleSensor(object):
    def __init__(self, device=DEVICE):
        self.device = device
        self.client = PMS5003(device=self.device)
        
    def read(self):
        try:
            pm_values = self.client.read()
        except ReadTimeoutError:
            pms5003.reset()
            pm_values = self.client.read()
        
        return {"pm_ug_per_m3_1_atm" : pm_values.pm_ug_per_m3(1.0,True),
        "pm_ug_per_m3_1_atm" : pm_values.pm_ug_per_m3(1.0,True),
        "pm_ug_per_m3_2_5_atm" : pm_values.pm_ug_per_m3(2.5,True),
        "pm_ug_per_m3_atm" : pm_values.pm_ug_per_m3(None,True),
        "pm_ug_per_m3_1" : pm_values.pm_ug_per_m3(1.0,False),
        "pm_ug_per_m3_2_5" : pm_values.pm_ug_per_m3(2.5,False),
        "pm_ug_per_m3_10" : pm_values.pm_ug_per_m3(10,False),
        "pm_per_1l_air_0_3" : pm_values.pm_per_1l_air(0.3),
        "pm_per_1l_air_0_5" : pm_values.pm_per_1l_air(0.5),
        "pm_per_1l_air_1" : pm_values.pm_per_1l_air(1.0),
        "pm_per_1l_air_2_5" : pm_values.pm_per_1l_air(2.5),
        "pm_per_1l_air_5" : pm_values.pm_per_1l_air(5),
        "pm_per_1l_air_10" : pm_values.pm_per_1l_air(10)}
