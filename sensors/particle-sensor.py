#!/usr/bin/env python

import requests
import sys
from pms5003 import PMS5003, ReadTimeoutError

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

try:
    bus = SMBus(1)
except Exception as e:
    sys.stderr.write(e)
    exit(1)

# Create PMS5003 instance
try:
    pms5003 = PMS5003(device='/dev/ttyS0')
except Exception as e:
    sys.stderr.write(e)
    exit(1)

def read_values():
    try:
        pm_values = pms5003.read()
        return pm_values
    except ReadTimeoutError:
        pms5003.reset()
        pm_values = pms5003.read()
        return pm_values

sys.stdout.write(read_values())
exit(0)
