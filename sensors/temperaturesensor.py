# Install Adafruit_DHT
# sudo pip3 install Adafruit_DHT

import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

class TemperatureSentor(object):
    def __init__(self, pin=DHT_PIN):
        self.pin = pin

    def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        return {"humidity": humidity, "temperatur": temperature}

# humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
# if humidity is not None and temperature is not None:
    # sys.stdout.write("[{0:0.1f}, {1:0.1f}]".format(temperature, humidity))
    # exit(0)
# else:
    # sys.stderr.write("Failed reading sensor")
    # exit(1)
