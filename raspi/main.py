import time
import board
import digitalio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = board.I2C()
ads = ADS.ADS1115(i2c)

chan = AnalogIn(ads, ADS.P0)

try:
    while True:
        try:
            water_level = chan.value
            print("Water Level:", water_level)
            time.sleep(0.5)
        except KeyboardInterrupt:
            break
except:
    print("Something is wrong!!! check if the connections to the sensors are correct.")

ads.deinit()