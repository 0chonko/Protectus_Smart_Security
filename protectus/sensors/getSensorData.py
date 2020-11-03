import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115(address=0x49)
adc2 = Adafruit_ADS1x15.ADS1115(address=0x48)

class getSensorData(object):

    def __init__(self,val):
        self.val = 0
        print('sensor data readings init')

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.

    #the following function get as input the gain value with wich the sensor data will be amplified, and the rate of trasmission
    #of the data.

    #cout is there for debugging purposes, if 1 the value is printed

    def read_gas_sensor_one(self, gain, dataRate, cout):
        value = adc2.read_adc(0,gain=gain) / 10000
        if (cout == 1):
            print('gas measurement on sensor one: ' + str(value))
        #allert trigger
        if value > 0.5:
            print ('alert gas sensor one')
        return value

    def read_gas_sensor_two(self, gain, dataRate, cout):
        value = adc2.read_adc(1, gain=gain) * 3.7 / 10000
        if (cout == 1):
            print('gas measurement on sensor two: ' + str(value))
        # allert trigger
        if value > 0.6:
            print('alert gas sensor two')
        return value

    def read_motion_sensor_one(self, gain, dataRate, cout):
        value = adc2.read_adc(2, gain=gain)
        if (cout == 1):
            print('motion measurement on sensor one: ' + str(value))
        # allert trigger
        if value > 1000:
            value = 1
            print ("motion detected on sensor one")
        else:
            value = 0
        return value

    def read_motion_sensor_two(self, gain, dataRate, cout):
        value = adc2.read_adc(3, gain=gain)
        if (cout == 1):
            print('motion measurement on sensor two: ' + str(value))
        # allert trigger
        if value > 100:
            value = 1
            print ("motion detected on sensor two")
        else:
            value = 0
        return value

    def read_microphone_sensor_one(self, gain, dataRate, cout):
        value = adc.read_adc(0, gain=gain)
        if (cout == 1):
            print('sound measurement on sensor one: ' + str(value))
        return value

    def read_microphone_sensor_two(self, gain, dataRate, cout):
        value = adc.read_adc(1, gain=gain)
        if (cout == 1):
            print('sound measurement on sensor two: ' + str(value))
        return value

    def read_sensor_bell(self, gain, dataRate, cout):
        value = adc.read_adc(2, gain=gain)
        if (cout == 1):
            print('measurement on bell sensor: ' + str(value))
        # allert trigger
        if value < 500:
            value = 0
            print("someone is at the door")
        return value

    def read_sensor_8(self, gain, dataRate, cout):
        value = adc.read_adc(3, gain=gain)
        if (cout == 1):
            print('extra measurement on sensor two: ' + str(value))
        return value


